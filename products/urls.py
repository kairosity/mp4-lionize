from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('seo-products', views.seo, name='seo-products'),
    path('content-creation-products', views.content_creation_products, name='content-creation-products'),
    path('web-design-products', views.webdesign, name='web-design-products'),
    path('<int:product_id>', views.product_detail, name='product_detail'),
]
