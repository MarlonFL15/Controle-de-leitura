from django.contrib import admin
from .models import *
# Register your models here.

#Define que quando ele mostrar a tela do autor, embaixo ele vai mostrar os posts do autor (em formato de pilha)
class LivroStacked(admin.StackedInline):
    model = Livro

class LivroAdmin(admin.ModelAdmin):
    inlines = (Livro, )

#class GeneroAdmin(admin.ModelAdmin):

admin.site.register(Genero)
admin.site.register(Livro)
#admin.site.register(Genero, GeneroAdmin)