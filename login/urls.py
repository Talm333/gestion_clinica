from django.urls import path
from .views import login, logout

urlpatterns = [
    path('login/login.html', login, name='login'),
    path('login/logout/', logout, name='logout'),
]