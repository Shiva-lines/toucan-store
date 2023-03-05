from django.shortcuts import render
from django.views import generic

# Create your views here.

class MainPage(generic.ListView):
    template_name = 'home.html'

    def get_queryset(self):
        pass