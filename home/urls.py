from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('#contact-us', views.index, name='contact'),
    path('webdesign', views.webdesign, name='webdesign'),
    path('seo', views.seo, name='seo'),
    path('social-media-management', views.social_media_management, name='social-media-management'),
    path('content-creation', views.content_creation, name='content-creation'),
    path('admin-product-dashboard', views.admin_dash_products, name='admin-dash-products'),
    path('admin-user-dashboard', views.admin_dash_users, name='admin-dash-users'),
    path('admin-messages-dashboard', views.admin_dash_messages, name='admin-dash-messages'),
]