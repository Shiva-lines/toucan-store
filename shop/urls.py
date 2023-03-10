from django.urls import path
from . views import *

urlpatterns = [
    path('', home, name='home'),
    path('privacytools', privacytools, name='privacytools'),
    path('faq', faq, name='faq'),
    path('blog', blog, name='blog'),
    path('account', account, name='account'),
    path('login', Login.as_view(), name='login'),
    path('register', register, name='register'),
    path('buy', buy, name='buy')
]

handler404 = error_404