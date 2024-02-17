from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


class UserRegistrationForm(UserCreationForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-form', 'type': 'text', 'placeholder': 'Имя'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-form', 'type': 'text', 'placeholder': 'Фамилия'
    }))
    surname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-form', 'type': 'text', 'placeholder': 'Отчество'
    }))
    number_class = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-form', 'type': 'text', 'placeholder': 'Класс'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-form', 'type': 'text', 'placeholder': 'Имя пользователя'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'input-form', 'type': 'email', 'placeholder': 'Электронная почта'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input-form', 'type': 'password', 'placeholder': 'Пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input-form', 'type': 'password', 'placeholder': 'Повторите пароль'
    }))
    school = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-form', 'type': 'text', 'placeholder': 'Школа'
    }))
    is_teacher = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'input-form', 'type': 'checkbox'
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'surname',
                  'username', 'email', 'is_teacher',
                  'number_class', 'school', 'password1',
                  'password2'
                  )


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-form', 'type': 'text', 'placeholder': 'Имя пользователя'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input-form', 'type': 'password', 'placeholder': 'Пароль'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')
