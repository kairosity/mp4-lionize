import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product

class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False) #is this needed? 
    date = models.DateField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    vat_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        '''
        Generate a random, unique order number using UUID.
        '''
        return uuid.uuid4().hex.upper()


    def update_total(self):
        '''
        Update grand total each time a line item is added, accounting for vat.
        '''
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
        self.vat_total = self.lineitems.aggregate(Sum('lineitem_vat'))['lineitem_vat__sum']
        self.grand_total = self.order_total + self.vat_total
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
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
    lineitem_vat = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
    lineitem_grand_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        '''
        Override the original save method to set the lineitem total and update the order total.
        '''
        self.lineitem_total = self.product.price * self.quantity
        self.lineitem_vat = float(self.lineitem_total) * float(0.23)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.order.order_number