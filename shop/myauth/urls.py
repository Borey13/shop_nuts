from django.contrib.auth.views import LoginView
from .views import AboutMeView, RegisterView, MyLogoutView
from django.urls import path
from . import views

app_name = 'myauth'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='myauth/login.html', redirect_authenticated_user=True), name='Login'),
    path('logout/', MyLogoutView.as_view(), name='Logout'),
    path('about-me/', AboutMeView.as_view(), name='About-me'),
    path('register/', RegisterView.as_view(), name='Register'),
    path('profile/', views.profile, name='profile'),
]
