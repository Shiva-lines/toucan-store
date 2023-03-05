from django.shortcuts import render
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from . forms import * 
from django.urls import reverse_lazy
 

# Create your views here.

def home(request):
    return render(request, 'home.html')

def privacytools(request):
    return render(request, 'privacytools.html')

def faq(request):
    return render(request, 'faq.html')

def blog(request):
    return render(request, 'blog.html')

def account(request):
    return render(request, 'account.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def error_404(request, exception):
    return render(request, '404.html')

class Login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')