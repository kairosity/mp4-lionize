from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('webdesign', views.webdesign, name='webdesign'),
    path('seo', views.seo, name='seo'),
    path('social-media-management', views.social_media_management, name='social-media-management'),
    path('content-creation', views.content_creation, name='content-creation'),
    path('pricing', views.pricing, name='pricing'),
]