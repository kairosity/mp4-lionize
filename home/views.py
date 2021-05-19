from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings
from django.contrib import messages

import os
# Create your views here.

def index(request):
    '''
    A view to return the main homepage.
    '''
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, [os.getenv('DEFAULT_FROM_EMAIL')])
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

def pricing(request):
    '''
    A view to return the content creation information page.
    '''
    return render(request, 'home/pricing.html')