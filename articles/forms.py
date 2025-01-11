from django import forms
from .models import Article



class ArticleCreateForm(forms.ModelForm):
    title = forms.CharField(min_length=5, label='Заголовок')
    class Meta:
        model = Article
        fields = ['title', 'content', 'photo', 'category', 'status', 'tags']
