from django.contrib import admin
from .models import Article, Category
from django.utils.safestring import mark_safe


@admin.register(Article)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['author', 'title','category', 'status', 'time_update']
    list_display_links = ['author']
    list_editable = ['status']
    fields = ['author', 'title', 'slug', 'content', 'photo', 'category', 'status']
    readonly_fields = ['slug']
    ordering = ['-time_update']
    list_filter = ['author', 'category', 'status']
    search_fields = ['title']
    search_help_text = 'Поиск по заголовку'

    @admin.display(description="Изображение", ordering='content')
    def post_photo(self, article: Article):
        if article.photo:
            return mark_safe(f"<img src='{article.photo.url}' width=50>")
        return "Без фото"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_display_links = ['name']
    readonly_fields = ['slug']
