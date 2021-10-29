from django.urls import path

from .views import *
urlpatterns = [
    path('leituras', leituras, name='leituras')
]