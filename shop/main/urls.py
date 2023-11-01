from django.urls import path
from . import views
from .views import AdminsView

app_name = 'main'

urlpatterns = [
    path('', views.main, name='main'),
    path('about-us', views.about, name='about'),
    path('search', views.search_results, name='search_results'),
    path('admin/', AdminsView.as_view(), name='admins'),
    path('category/<int:id_cat>', views.category, name='category'),
    path('product/<int:id_prod>', views.product, name='product'),
]
