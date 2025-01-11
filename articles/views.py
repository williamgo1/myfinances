from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ArticleCreateForm
from .models import Article
from django.contrib.auth import get_user_model, logout
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse


class ArticleListView(ListView):
    extra_context = {'title': 'Все статьи'}
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.published.all()


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'

    def get_object(self, queryset = None):
        return Article.objects.get(slug=self.kwargs.get(self.slug_url_kwarg, None))


class ArticleCreateView(LoginRequiredMixin, CreateView):
    form_class = ArticleCreateForm
    template_name = 'articles/create_article.html'
    extra_context = {'title': 'Создание статьи'}

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    pass


class MyArticleListlView(ListView):
    template_name = 'articles/article_list.html'