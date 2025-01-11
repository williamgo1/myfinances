from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    path('create-article/', views.ArticleCreateView.as_view(), name='create_article'),
    path('article-list/', views.ArticleListView.as_view(), name='article_list'),
    path('my-articles/', views.MyArticleListlView.as_view(), name='my_articles'),
    path('<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
]