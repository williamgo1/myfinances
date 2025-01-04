from django.views.generic import ListView, FormView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model


class HomePageView(ListView):
    model = get_user_model()
    template_name = 'finances/index.html'

