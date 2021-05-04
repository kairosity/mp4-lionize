from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import os
import stripe

def checkout(request):
    stripe_public_key = os.getenv('STRIPE_PUBLIC_KEY')
    stripe_secret_key = os.getenv('STRIPE_SECRET_KEY')

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment.")
        return redirect(reverse('products'))
    
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': stripe_secret_key,
    }

    return render(request, template, context)
