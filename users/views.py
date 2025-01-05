from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.views import PasswordChangeView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserCreateForm, UserLoginForm, UserProfileForm, UserPasswordChangeForm

from django.contrib.auth import get_user_model, logout
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect


class UserProfileView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    extra_context = {'title': 'Профиль'}
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    extra_context = {'title': 'Регистрация'}


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}
    success_url = reverse_lazy('users:profile')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))


class UserPasswordChangeView(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'users/password_change_form.html'
    extra_context = {'title': 'Изменение пароля'}
    success_url = reverse_lazy('users:password_change_done')
