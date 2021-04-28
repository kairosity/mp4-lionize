from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'price',
    )

    ordering = ('category',)

admin.site.register(Product, ProductAdmin)


