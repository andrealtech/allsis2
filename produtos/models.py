from django.db import models


class TipoProduto(models.Model):
    tipo = models.CharField(max_length=10)

    def __str__(self):
        return self.tipo
    

class Produtos(models.Model):
    nome = models.CharField(max_length=20)
    tipo = models.ForeignKey(TipoProduto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    