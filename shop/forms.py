from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={}))
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={}),
            'password': forms.PasswordInput(attrs={}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget= forms.TextInput(attrs={}))
    password = forms.CharField(label='Password', widget= forms.PasswordInput(attrs={}))

