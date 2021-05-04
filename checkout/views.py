from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment.")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51InQT1G54ev3bb3zz0PsP9ohVaKvdXgbgusNmlsEDYHdDZScHQEJ5GzfEltSJ37aotzc45iAENmm4vicxgMOk5CY00DDXyQNXU',
        'client_secret': 'not a real password',
    }

    return render(request, template, context)
