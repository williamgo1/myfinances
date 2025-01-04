from django.views.generic import ListView, FormView, CreateView
from django.contrib.auth.views import LoginView
from .forms import UserCreateForm, UserLoginForm, UserProfileForm
from django.contrib.auth import get_user_model, logout
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect



class UserProfileView(FormView):
    form_class = UserProfileForm
    template_name = 'accounts/profile.html'
    extra_context = {'title': 'Профиль'}


class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('users:login')
    extra_context = {'title': 'Регистрация'}
    

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'registration/login.html'
    extra_context = {'title': 'Авторизация'}
    success_url = reverse_lazy('users:profile')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))
