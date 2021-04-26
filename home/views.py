from django.shortcuts import render

# Create your views here.

def index(request):
    '''
    A view to return the main homepage.
    '''
    return render(request, 'home/index.html')

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