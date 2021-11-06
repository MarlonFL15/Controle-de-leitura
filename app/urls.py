from django.urls import path

from .views import *
urlpatterns = [
    path('leituras', leituras, name='leituras'),
    path('cadastrar_leitura', cadastrar_leitura, name='cadastrar_leitura'),
    path('visualizar_leitura/<int:id>', visualizar_leitura, name='visualizar_leitura'),
    path('editar_leitura/<int:id>', editar_leitura, name='editar_leitura'),
    path('deletar_leitura/<int:id>', deletar_leitura, name='deletar_leitura'),

]