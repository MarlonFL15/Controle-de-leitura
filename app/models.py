from django.db import models
# Create your models here.

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
        ("N", "Não iniciado"),
        ("LE", "Em leitura"),
        ("LI", "Lido")
    )
    livro = models.ManyToManyField(Livro)
    status = models.CharField(blank=False, max_length=2, null=False, choices=STATUS_CHOICES)
    nota = models.IntegerField(null=True)

