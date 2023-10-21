from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import RegisterUserForm, LoginUserForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


class AboutMeView(TemplateView):
    template_name = "myauth/about-me.html"


class LoginView(CreateView):
    form_class = LoginUserForm
    template_name = "myauth/login.html"
    success_url = reverse_lazy("myauth:About-me")


class RegisterView(CreateView):
    form_class = RegisterUserForm
    template_name = "myauth/register.html"
    success_url = reverse_lazy("myauth:About-me")

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(self.request, username=username, password=password)
        login(request=self.request, user=user)
        return response


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("myauth:Login")


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('myauth:About-me')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'myauth/profile.html', context)
