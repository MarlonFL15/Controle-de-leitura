from django.db import models
# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .manager import UsuarioManager

# Create your models here.

class Usuario(AbstractBaseUser, PermissionsMixin):
    objects = UsuarioManager()
    nome = models.CharField(max_length=100, null=True, blank=False)
    email = models.EmailField(unique=True, max_length=30, null=False, blank=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email' #campo utilizado ao invés de "username" para fazer o login
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.email


class Genero(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=50, null=False, blank=False)
    autor = models.CharField(max_length=50, null=False, blank=False)
    generos = models.ManyToManyField(Genero)

    def __str__(self):
        return self.titulo

class Leitura(models.Model):
    STATUS_CHOICES = (
        ("N", "Pretendo ler"),
        ("LE", "Em leitura"),
        ("LI", "Lido")
    )
    livro = models.ForeignKey(Livro, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    status = models.CharField(blank=False, max_length=2, null=False, choices=STATUS_CHOICES)
    nota = models.IntegerField(null=True, blank=True, default=0)
    resenha = models.TextField(blank=True, null=True)

    @property
    def get_status(self):
        return self.get_status_display()

