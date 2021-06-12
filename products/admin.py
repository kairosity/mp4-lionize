from django.contrib import admin
from .models import Product, Review

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'price',
        'image',
    )

    ordering = ('category',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'review_stars',
        'review_title',
        'review',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)


