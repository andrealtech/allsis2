from django.db import models


class Produtos(models.Model):
    nome = models.CharField(max_length=20)
    tipo = models.CharField(max_length=10)

    def __str__(self):
        return self.nome
    