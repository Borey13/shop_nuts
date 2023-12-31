from django.urls import path
from . import views


app_name = 'cart'

urlpatterns = [
    path('detail', views.cart_detail, name='cart_detail'),
    path('cart_add/<product_id>', views.cart_add, name='cart_add'),
    path('cart_remove/<product_id>', views.cart_remove, name='cart_remove'),
]