from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    ano_lancamento = models.IntegerField()
    sinopse = models.TextField()

    def _str_(self):
        return self.titulo