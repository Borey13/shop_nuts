from django.urls import path
from . import views

urlpatterns = [
    path('main', views.main),
    path('about-us', views.about),
    path('category', views.category),
    path('product', views.product)
]
