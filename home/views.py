from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import ContactForm
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from profiles.models import UserProfile, Message
from products.models import Product, Category
from django.db.models import Q

import os
# Create your views here.

def error_page(request):
    '''
    A view to test the error pages.
    '''
    return render(request, '403.html')

def index(request):
    '''
    A view to return the main homepage.
    '''
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if request.user.is_authenticated:
            user = get_object_or_404(UserProfile, user=request.user)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, [os.getenv('DEFAULT_FROM_EMAIL')])
                
                if request.user.is_authenticated:
                    messages.success(request, (
                        "Your email was delivered. Thank you. Lionize will get back to you within 36 hours. Please note that a copy of this email is saved in our database. In accordance with GDPR legislation, should you wish for us to delete this message, please let us know.")
                    )
                    new_message = Message(user=user, subject=subject, message=message)
                    new_message.save()
                else:
                    messages.success(request, (
                        "Your email was delivered. Thank you. Lionize will get back to you within 36 hours.")
                    )
            except BadHeaderError:
                messages.error(request, (
                        "I'm afraid there was an issue sending your message, please try again.")
                    )
                return HttpResponse('Invalid header found.')
            return redirect('home')
    
        
    return render(request, 'home/index.html', {'form': form})

def webdesign(request):
    '''
    A view to return the web design information page.
    '''
    return render(request, 'home/webdesign.html')

def seo(request):
    '''
    A view to return the seo information page.
    '''
    return render(request, 'home/seo.html')

def social_media_management(request):
    '''
    A view to return the social media management information page.
    '''
    return render(request, 'home/social_media_management.html')

def content_creation(request):
    '''
    A view to return the content creation information page.
    '''
    return render(request, 'home/content_creation.html')

@login_required
def admin_dash_products(request):
    '''
    A view to return the admin products dashboard. Only available & visible to logged in admin users.
    '''

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, but you are not authorized to view this page. If you have an admin account, please login and try again.')
        return HttpResponseForbidden()

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
                messages.error(request, "You did enter a search term.")
                return redirect(reverse('admin-dash-products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(friendly_name__icontains=query) | Q(features__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'home/admin_dash_products.html', context)

@login_required
def admin_dash_users(request):
    '''
    A view to return the admin users dashboard. Only available & visible to logged in admin users.
    '''

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, but you are not authorized to view this page. If you have an admin account, please login and try again.')
        return HttpResponseForbidden()

    user_profiles = UserProfile.objects.all()
    user_messages = Message.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did enter a search term.")
                return redirect(reverse('admin-dash-users'))
            
            queries = Q(user__username__icontains=query) | Q(user__first_name__icontains=query) | Q(user__last_name__icontains=query) | Q(user__email__icontains=query)
            user_profiles = user_profiles.filter(queries)

    context = {
        'user_profiles': user_profiles,
        'user_messages': user_messages,
        'search_term': query,
    }

    return render(request, 'home/admin_dash_users.html', context)