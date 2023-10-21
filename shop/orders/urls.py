from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create', views.order_create, name='order_create'),
    path('my_orders', views.my_orders, name='my_orders'),
    path('my_orders_items/<int:id>', views.my_orders_items, name='my_orders_items'),
]
