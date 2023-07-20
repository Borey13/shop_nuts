from django.urls import path
from . import views

urlpatterns = [
    path('main', views.main, name='Main'),
    path('about-us', views.about, name='About'),
    path('category/<int:id_cat>', views.category, name='Category'),
    path('product/<int:id_prod>', views.product, name='Product')
]
