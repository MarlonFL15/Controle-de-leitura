from django.urls import path

from .views import *
urlpatterns = [
    path('leituras', leituras, name='leituras'),
    path('cadastrar_leitura', cadastrar_leitura, name='cadastrar_leitura'),
]