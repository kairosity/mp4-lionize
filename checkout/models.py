import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField
from products.models import Product
from profiles.models import UserProfile
from lionize.validations import validate_phone_number


class Order(models.Model):
    '''
    For saving order details from user purchases from the shop.
    '''
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, 
                                    null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False, validators=[validate_phone_number])
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    vat_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')


    def _generate_order_number(self):
        '''
        Generate a random, unique order number using UUID.
        '''
        return uuid.uuid4().hex.upper()

    def update_total(self):
        '''
        Update grand total each time a line item is added, accounting for vat.
        '''
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.vat_total = self.lineitems.aggregate(Sum('lineitem_vat'))['lineitem_vat__sum'] or 0
        self.grand_total = self.order_total + self.vat_total or 0
        self.save()

    def save(self, *args, **kwargs):
        '''
        Override the original save method to set the order number if it has not already been set.
        '''
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    '''
    Each unique product ordered in the "Order" model above is saved to the database as an Order Line Item.
    '''
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
    lineitem_vat = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
    lineitem_grand_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
    reviewed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        '''
        Override the original save method to set the lineitem total and update the vat & order totals.
        '''

        self.lineitem_total = self.product.price * self.quantity
        self.lineitem_vat = float(self.lineitem_total) * float(0.23)
        self.lineitem_grand_total = float(self.lineitem_total) + float(self.lineitem_vat)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.order.order_number
