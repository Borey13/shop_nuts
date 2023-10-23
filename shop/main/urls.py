from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('main', views.main, name='main'),
    path('about-us', views.about, name='About'),
    path('search', views.search_results, name='search_results'),
    path('category/<int:id_cat>', views.category, name='Category'),
    path('product/<int:id_prod>', views.product, name='Product'),
]
