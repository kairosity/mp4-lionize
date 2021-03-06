from django.core.mail import send_mail, BadHeaderError
from django.core.exceptions import PermissionDenied
from django.http import (HttpResponse,
                         HttpResponseRedirect,
                         HttpResponseForbidden)
from django.shortcuts import (render,
                              redirect,
                              reverse,
                              get_object_or_404)
from .forms import ContactForm
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from profiles.models import UserProfile, Message
from products.models import Product, Category
from django.db.models import Q

import os


def index(request):
    '''
    * Displays homepage template & allows users to send emails.
    * If user is logged in, email form is pre-filled with their
    email address.
    \n Args:
    1. request object
    \n Returns:
    * Template displaying the homepage
    * POST method sends Lionize an email.
    '''
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if request.user.is_authenticated:
            user = get_object_or_404(UserProfile, user=request.user)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message_body = form.cleaned_data['message']
            message = f'Email from: {email} \nMessage: {message_body}'
            try:
                send_mail(subject, message, email,
                          [settings.DEFAULT_FROM_EMAIL])

                if request.user.is_authenticated:
                    messages.success(request, (
                        "Your email was delivered. Thank you. Lionize will\
                        get back to you within 36 hours. Please note that a\
                        copy of this email is saved in our database. In \
                        accordance with GDPR legislation, should you wish \
                        for us to delete this message, please let us know.")
                    )
                    new_message = Message(
                        user=user, subject=subject, message=message)
                    new_message.save()
                else:
                    messages.success(request, (
                        "Your email was delivered. Thank you.\
                        Lionize will get back to you within 36 hours.")
                    )
            except BadHeaderError:
                messages.error(request, (
                        "I'm afraid there was an issue sending your\
                        message, please try again.")
                    )
                return HttpResponse('Invalid header found.')
            return redirect('home')

    return render(request, 'home/index.html', {'form': form})


def webdesign(request):
    '''
    * Displays the web design information page.
    \n Args:
    1. request object
    \n Returns:
    * Template displaying the web design information page.
    '''
    return render(request, 'home/webdesign.html')


def seo(request):
    '''
    * Displays the seo information page.
    \n Args:
    1. request object
    \n Returns:
    * Template displaying the seo information page.
    '''
    return render(request, 'home/seo.html')


def social_media_management(request):
    '''
    * Displays the social media management information page.
    \n Args:
    1. request object
    \n Returns:
    * Template displaying the social media management information page.
    '''
    return render(request, 'home/social_media_management.html')


def content_creation(request):
    '''
    * Displays the content creation information page.
    \n Args:
    1. request object
    \n Returns:
    * Template displaying the content creation information page.
    '''
    return render(request, 'home/content_creation.html')


@login_required
def admin_dash_products(request):
    '''
    * A view to return the admin products dashboard.
    * Only available & visible to logged in admin users.
    \n Args:
    1. request object
    \n Returns:
    * Template displaying the admin products dashboard.
    * If search form is used: returns search results using
    Q object.
    '''
    if not request.user.is_staff:
        messages.error(request, 'Sorry, but you are not authorized\
            to view this page. If you have an admin account, please\
                login and try again.')
        raise PermissionDenied()

    products = Product.objects.all()
    query = None
    category = None

    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category']
            products = products.filter(category__name=category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter a search term.")
                return redirect(reverse('admin-dash-products'))

            queries = Q(name__icontains=query) | \
                Q(description__icontains=query) | \
                Q(friendly_name__icontains=query) | \
                Q(features__icontains=query)
            products = products.filter(queries)

            if not products:
                messages.warning(request, "There were no\
                    results for your search term.")

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'home/admin_dash_products.html', context)


@login_required
def admin_dash_users(request):
    '''
    * A view to return the admin users dashboard.
    * Only available & visible to logged in admin users.
    \n Args:
    1. request object
    \n Returns:
    * Template displaying the admin users dashboard.
    * If search form is used: returns search results using
    Q object.
    '''

    if not request.user.is_staff:
        messages.error(request, 'Sorry, but you are not authorized\
                to view this page. If you have an admin account,\
                please login and try again.')
        raise PermissionDenied()

    user_profiles = UserProfile.objects.all()
    user_messages = Message.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter a search term.")
                return redirect(reverse('admin-dash-users'))

            queries = Q(user__username__icontains=query) | \
                Q(user__first_name__icontains=query) | \
                Q(user__last_name__icontains=query) | \
                Q(user__email__icontains=query)
            user_profiles = user_profiles.filter(queries)

            if not user_profiles:
                messages.warning(request, "No users were returned\
                    for that search term.")

    context = {
        'user_profiles': user_profiles,
        'search_term': query,
    }
    return render(request, 'home/admin_dash_users.html', context)


@login_required
def admin_dash_messages(request):
    '''
    * A view to return the admin messages dashboard.
    * Only available & visible to logged in admin users.
    \n Args:
    1. request object
    \n Returns:
    * Template displaying the admin messages dashboard.
    '''

    if not request.user.is_staff:
        messages.error(request, 'Sorry, but you are not authorized\
                to view this page. If you have an admin account,\
                please login and try again.')
        raise PermissionDenied()

    user_profiles = UserProfile.objects.all()
    user_messages = Message.objects.all().order_by('-date')

    context = {
        'user_messages': user_messages,
    }

    return render(request, 'home/admin_dash_messages.html', context)
