from django.urls import path
from . import views 

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('orders', views.order_history_user_portal, name='user_orders'),
    path('reviews', views.your_reviews, name='reviews'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('mark-active/<int:message_id>/', views.mark_active, name='mark_active'),
    path('mark-closed/<int:message_id>/', views.mark_closed, name='mark_closed'),
]