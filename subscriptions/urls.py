from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_subscriptions, name='subscriptions'),
    path('social-media-management-subscriptions', views.social_media_management_subscriptions, name='social-media-management-subscriptions'),
    path('<id>', views.product_detail, name='product_detail'),
]