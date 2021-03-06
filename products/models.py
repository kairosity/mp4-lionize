from django.db import models
from categories.models import Category
from profiles.models import UserProfile
from django.core.validators import MaxValueValidator, MinValueValidator
from lionize.validations import (validate_min_length_2,
                                validate_min_length_50,
                                validate_min_length_20,
                                validate_text_input,
                                )


class Product(models.Model):
    '''
    Each product potentially for sale in the shop is saved with these details.
    '''
    category = models.ForeignKey('categories.Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254, validators=[validate_min_length_2, validate_text_input])
    friendly_name = models.CharField(max_length=254, validators=[validate_min_length_2, validate_text_input])
    description = models.TextField(max_length=500, validators=[validate_min_length_50, validate_text_input])
    features = models.TextField(max_length=1200, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    in_shop = models.BooleanField(null=False, blank=False, default=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class Review(models.Model):
    '''
    For every unique product type a user orders, they can write a review of that product.
    '''

    CHOICES = (
        ('option1', '1 Star'), ('option2', '2 Stars'), ('option3', '3 Stars'), ('option4', '4 Stars'), ('option5', '5 Stars')
    )
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_reviews')
    user = models.ForeignKey('profiles.UserProfile', on_delete=models.CASCADE, related_name='user_reviews')
    review_title = models.CharField(max_length=120, null=True, blank=False, validators=[validate_min_length_2])
    review = models.TextField(max_length=500, null=True, blank=False, validators=[validate_min_length_20])
    review_stars = models.CharField(max_length=70, choices = CHOICES, default = 'option5')
    date_reviewed = models.DateField(auto_now=True)