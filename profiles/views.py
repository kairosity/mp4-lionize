from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from .models import UserProfile, Message
from products.models import Review
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request):
    '''
    * A view to display the user profile page and form.
    * Only available & visible to logged in users.
    \n Args:
    1. request object
    \n Returns:
    * Template displaying the user profile form.
    '''
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            # Save the first & last name from the profile to
            # the Django user auth form.
            User = get_user_model()
            user_to_update = get_object_or_404(User, username=request.user)
            user_to_update.first_name = form.cleaned_data['default_first_name']
            user_to_update.last_name = form.cleaned_data['default_last_name']
            user_to_update.save()

            messages.success(request, 'Profile updated successfully!')
        else:
            messages.error(request, f'Update failed, please ensure\
                your form entries are valid and then try again.')
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'

    context = {
        'form': form,
        'on_profile_page': True,
    }

    return render(request, template, context)


@login_required
def order_history_user_portal(request):
    '''
    * A view to display the user's order history.
    * Only available & visible to logged in users.
    \n Args:
    1. request object
    \n Returns:
    * Template displaying the user's order history'.
    '''

    profile = get_object_or_404(UserProfile, user=request.user)

    orders = profile.orders.all().order_by('-date')

    template = 'profiles/orders.html'

    context = {
        'orders': orders,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    '''
    * A view to display specific order details.
    * Only available & visible to logged in users.
    \n Args:
    1. request object
    2. order number
    \n Returns:
    * Template displaying the details of a specific order.
    '''
    order = get_object_or_404(Order, order_number=order_number)

    referring_page = '/user-portal/orders'

    if str(request.user.username) != str(order.user_profile):
        messages.error(request, "Sorry, but you are not permitted\
            to view another user's order history.")
        raise PermissionDenied()

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
        'referring_page': referring_page,
    }

    return render(request, template, context)


@login_required
def your_reviews(request):
    '''
    * A view to display the user's reviews page.
    * Only available & visible to logged in users.
    \n Args:
    1. request object
    \n Returns:
    * Template displaying the products a user can review.
    * And the reviews they have already written.
    '''

    profile = get_object_or_404(
        UserProfile, user=request.user)
    orders = profile.orders.all()
    reviews = Review.objects.filter(
        user=profile).order_by('-date_reviewed')

    template = 'profiles/your_reviews.html'
    context = {
        'orders': orders,
        'reviews': reviews,
    }

    return render(request, template, context)


@login_required
def mark_closed(request, message_id):
    '''
    * Mark a message as closed.
    * Functionality only available to admin users.
    \n Args:
    1. request object
    2. message id
    \n Returns:
    * Marks a message as closed.
    '''

    if not request.user.is_staff:
        messages.error(request, 'Sorry, but you are not authorized\
            to edit message status! If you have an admin account,\
            please login.')
        raise PermissionDenied()

    message = get_object_or_404(Message, pk=message_id)
    message.resolved = True
    message.save()
    messages.success(request, f'That message issue has\
        been successfully marked as resolved.')
    return redirect(reverse('admin-dash-messages'))


@login_required
def mark_active(request, message_id):
    '''
    * Mark a message as re-opened.
    * Functionality only available to admin users.
    \n Args:
    1. request object
    2. message id
    \n Returns:
    * Marks a message as open again.
    '''

    if not request.user.is_staff:
        messages.error(request, 'Sorry, but you are not\
            authorized to edit message status! If you have\
            an admin account, please login.')
        raise PermissionDenied()

    message = get_object_or_404(Message, pk=message_id)
    message.resolved = False
    message.save()
    messages.success(request, f'That message issue\
        has been successfully re-opened.')
    return redirect(reverse('admin-dash-messages'))
