from django.urls import path
from .views import login, logout

urlpatterns = [
<<<<<<< HEAD
=======
    path('', login, name='inicio'),
>>>>>>> e99703f12acfebac4082134a4372a8fcc356d997
    path('login/login.html', login, name='login'),
    path('login/logout/', logout, name='logout'),
]