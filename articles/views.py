from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ArticleCreateForm
from .models import Article


class ArticleListView(ListView):
    extra_context = {'title': 'Все статьи'}
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    paginate_by = 5

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
        obj = form.save(commit=False)
        obj.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'articles/edit_article.html'
    extra_context = {'title': 'Редактирование статьи'}
    fields = ["title", "content", "photo", "category", "status", "tags"]


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = "articles/delete_article.html"
    extra_context = {'title': 'Удаление статьи'}
    success_url = reverse_lazy("articles:article_list")


class MyArticleListlView(LoginRequiredMixin, ListView):
    extra_context = {'title': 'Мои статьи'}
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    paginate_by = 5

    def get_queryset(self):
        return Article.objects.filter(author = self.request.user)