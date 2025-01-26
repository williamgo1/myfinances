from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    path('article-list/', views.ArticleListView.as_view(), name='article_list'),
    path('my-articles-list/', views.MyArticleListlView.as_view(), name='my_articles'),
    path('category/<slug:cat_slug>/', views.ArticleListView.as_view(), name='category'),

    path('create-article/', views.ArticleCreateView.as_view(), name='create_article'),
    path('edit/<slug:slug>/', views.ArticleUpdateView.as_view(), name='edit_article'),
    path('delete/<slug:slug>/', views.ArticleDeleteView.as_view(), name='delete_article'),
    path('<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
]