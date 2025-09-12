from django.urls import path
from .views import entrega

urlpatterns = [
    path('', entrega, name='entrega'),
]