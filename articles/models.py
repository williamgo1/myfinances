from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.validators import MinLengthValidator
from transliterate import slugify
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(db_index=True, unique=True, verbose_name='Категория')
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name='slug')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class PublishedArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=1)


class Article(models.Model):
    HIDDEN_STATUS = -1
    DRAFT_STATUS = 0
    PUBLISHED_STATUS = 1
    STATUS_CHOICES = (
        (HIDDEN_STATUS, 'Скрыто'),
        (DRAFT_STATUS, 'Черновик'),
        (PUBLISHED_STATUS, 'Опубликовано'),
    )
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, 
                               null=True, related_name='articles', verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Заголовок',
                             validators=[MinLengthValidator(5, message="Минимум 5 символов")])
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Slug')
    content = models.TextField(verbose_name='Текст статьи') # Textarea.
    photo = models.ImageField(upload_to="photos/%Y/%m/", blank=True, null=True, verbose_name='Фото статьи')
    time_create = models.DateTimeField(auto_now=True, verbose_name='Время создания') # DateInput.
    time_update = models.DateTimeField(auto_now_add=True, verbose_name='Время изменения')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, max_length=100, 
                                 related_name= 'articles', verbose_name='Категория')
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=DRAFT_STATUS, verbose_name='Статус')
    tags = TaggableManager(blank=True, verbose_name='Теги')

    objects = models.Manager()
    published = PublishedArticleManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ['-time_update']

    def get_absolute_url(self):
        return reverse('articles:article_detail', kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
