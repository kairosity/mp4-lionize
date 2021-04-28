from django.db import models
from categories.models import Category

class Subscription(models.Model):

    plans = (
		('BASIC', 'Monthly Basic (€450/Mo)'),
		('STANDARD', 'Monthly Standard (€950/Mo)'),
		('PREMIUM', 'Monthly Premium (€1500/Mo)'),
	)
    category = models.ForeignKey('categories.Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price_per_month = models.DecimalField(max_digits=6, decimal_places=2)
    plan_type = models.CharField(max_length=15, choices=plans, default='BASIC')

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name