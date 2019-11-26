from decimal import Decimal, ROUND_DOWN

from django.db import models


class Sabor(models.Model):
    nome_do_sabor = models.CharField(max_length=50)

    def __str__(self):
        """Deve ser retornado o valor do atributo nome_do_sabor."""

        return f'{self.nome_do_sabor}'


class Sorvete(models.Model):
    unidades = models.PositiveIntegerField('Unidades')
    sabores = models.ManyToManyField('Sabor')
    preco_de_venda = models.DecimalField(
        'Preço de venda',
        max_digits=6,
        decimal_places=2,
        default=Decimal('0')
    )
    preco_de_custo = models.DecimalField(
        'Preço de Custo',
        max_digits=6,
        decimal_places=2
    )

    def __str__(self):
        """Deve ser retornado todos os sabores e o valor de venda."""

        sabores = ''.join(str(sabor) for sabor in self.sabores.all())
        exibicao = f'{sabores} {str(self.preco_de_venda).replace(".", ",")}'
        return exibicao

    def calcula_preco_de_venda(self):
        """
        Calcula preco de venda de uma unidade do sorvete.

        As seguintes condições devem ser respeitada as seguintes regras
        para a precificação do sorvete:

         - Para 10 unidades de um sorvete cujo a somatória total do custo
         esteja entre 0 < valor <= 24.99. O Preço de venda será igual ao valor
         unitário + 10% do valor unitário;

         - Para 10 unidades de um sorvete cujo a somatória total do custo
         esteja entre 25 <= valor <= 49.99. O preço de venda será igual ao
         valor unitário + 20% do valor unitário;

         - Para 10 unidades de um sorvete curjo a somatória total do custo
         seja valor >= 50.00. O preço de venda será igual ao valor unitário +
         35% do valor unitário.
      """

        preco_de_custo = Decimal(self.preco_de_custo * 10)
        if preco_de_custo <= Decimal('24.99'):
            self.preco_de_venda = (
                    self.preco_de_custo + self.preco_de_custo * 0.1
            )
        elif Decimal('25') <= preco_de_custo <= Decimal('49.99'):
            self.preco_de_venda = (
                self.preco_de_custo + self.preco_de_custo * 0.2
            )
        else:
            self.preco_de_venda = (
                    self.preco_de_custo + self.preco_de_custo * 0.35
            )

        self.save()
        return Decimal(str(self.preco_de_venda)).quantize(
            Decimal('0.01'),
            rounding=ROUND_DOWN
        )
