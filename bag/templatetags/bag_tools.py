from django import template 

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity

@register.filter(name='vat')
def vat(price):
    return float(price) * float(0.23)

@register.filter(name='subtotalinclvat')
def subtotalinclvat(price, quantity):
    return  float(price) * float(quantity)  * float(1.23)