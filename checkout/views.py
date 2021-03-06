from django.shortcuts import (render,
                              redirect,
                              reverse,
                              get_object_or_404,
                              HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .forms import OrderForm
from bag.contexts import bag_contents
from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from .models import OrderLineItem, Order
from django.template.loader import render_to_string

import os
import stripe
import json


@require_POST
def cache_checkout_data(request):
    '''
    Caches the checkout data.
    '''
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


@login_required
def checkout(request):
    '''
    Processes the checkout form.
    \n Args:
    1. request object
    \n Returns:
    * Saves the order as an instance of the order model.
    * Saves each item in the order as an instance of the order
    line item model.
    * Pre-fills the checkout form with user profile data.
    * Creates a Stripe payment intent.
    '''
    stripe_public_key = os.getenv('STRIPE_PUBLIC_KEY')
    stripe_secret_key = os.getenv('STRIPE_SECRET_KEY')

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            # Converts python bag object into a json string to store on
            # the order model.
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found\
                        in our database."
                        "Please call us for assistance.")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))
            order.update_total()
            request.session['save_info'] = \
                'save-info' in request.POST

            # Send Confirmation Email 
            all_items = []
            for item in order.lineitems.all():
                all_items.append(item.product.friendly_name)

            newline = '\n - '

            cust_email = order.email
            subject = render_to_string(
                'checkout/confirmation_emails/confirmation_email_subject.txt',
                {'order': order})
            body = f"Hello {order.full_name}, \
                \n\nThank you for trusting Lionize with your digital presence!\n \
                \nYour order was processed successfully!\
                \n\nYou ordered the following products:\n - { newline.join(item for item in all_items) }.\
                \n\nSubtotal: ???{order.order_total}\
                \nVAT Total @23%: ???{order.vat_total}\
                \nGrand Total: ???{order.grand_total}\
                \n\nA more comprehensive breakdown of this order as well as a full order history can be found in the User Portal Order History section of our site. \n \
                \nJust login & navigate to your User Portal.\n\
                \nThank you again from all of us at Lionize!"
            
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [cust_email]
            )        

            return redirect(
                reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form.\
                Please double check your information')
        
            template = 'checkout/checkout.html'

            context = {
                'order_form': order_form,
                'stripe_public_key': stripe_public_key,
            }
            return render(request, template, context)

    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag\
                                      at the moment.")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        # Prefill the form with any info the user maintains in their profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(request, 'The stripe public key is missing.')

        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }
        return render(request, template, context)


@login_required
def checkout_success(request, order_number):
    '''
    Handles successful checkouts
    \n Args:
    1. request object
    2. order number
    \n Returns:
    * Renders the checkout success page.
    '''
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        split_order_name = order.full_name.split(' ')

        # Save the user's info
        if save_info:
            profile_data = {
                'default_first_name': split_order_name[0],
                'default_last_name': split_order_name[1],
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
                'instagram_handle': profile.instagram_handle,
                'linkedin_handle': profile.linkedin_handle,
                'facebook_handle': profile.facebook_handle,
                'twitter_handle': profile.twitter_handle,
                'consultation': profile.consultation,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed!\
        Your order number is {order_number}. A confirmation\
            email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
