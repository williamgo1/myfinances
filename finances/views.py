from django.views.generic import ListView, TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model


class HomePageView(ListView):
    model = get_user_model()
    template_name = 'finances/index.html'
    extra_context = {'title': 'Главная страница'}


class AboutView(TemplateView):
    template_name = 'finances/about.html'
    extra_context = {'title': 'О сайте'}