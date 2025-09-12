from django.urls import path
from .views import login

urlpatterns = [
    path('', login, name='login'),
    path('login/login.html', login, name='login'),
]