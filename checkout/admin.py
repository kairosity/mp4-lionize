from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total', 'lineitem_vat', 'lineitem_grand_total',)

class OrderAdmin(admin.ModelAdmin):

    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                        'order_total', 'vat_total',
                        'grand_total',)
    
    fields = ('order_number', 'date', 'full_name',
                'email', 'phone_number', 'country',
                'order_total', 'vat_total', 'grand_total')
            
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'vat_total', 'grand_total')

    
    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)