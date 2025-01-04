from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model


class UserCreateForm(UserCreationForm):
    username = forms.CharField(label='Логин', max_length=100)
    password1 = forms.CharField(label='Придумайте пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput())
    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль')

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

class UserProfileForm(forms.ModelForm):
    username = forms.CharField()
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username': 'Логин',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'email'
        }
