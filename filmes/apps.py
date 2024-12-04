from django.db import models
from django.apps import AppConfig

class FilmesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filmes'  # Nome do app deve ser exatamente o nome da pasta

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    ano_lancamento = models.IntegerField()
    sinopse = models.TextField()

    def _str_(self):
        return self.titulo