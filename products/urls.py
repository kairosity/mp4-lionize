from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('seo-products/', views.seo, name='seo-products'),
    path('content-creation-products/', views.content_creation_products, name='content-creation-products'),
    path('web-design-products/', views.webdesign, name='web-design-products'),
    path('social-media-management/', views.social_media_management, name='social_media_management'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('remove/<int:product_id>/', views.remove_from_shop, name='remove_from_shop'),
    path('addtoshop/<int:product_id>/', views.add_to_shop, name='add_to_shop'),
    path('edit-review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete-review/<int:review_id>/', views.delete_review, name='delete_review'),
]
