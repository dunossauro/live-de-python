from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    nome = models.CharField(max_length=30)
    categoria = models.ForeignKey(Categoria, null=True,
                                  on_delete=models.CASCADE)
    autor = models.CharField(max_length=30)
    em_estoque = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome

    def disponivel(self):
        return bool(self.em_estoque)
