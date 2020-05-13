from typing import Callable


class Item:
    def __init__(self, nome: str, valor: int):
        self.nome = nome
        self.valor = valor

    def __repr__(self):
        return f'Item(nome={self.nome}, valor={self.valor})'


class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item: Item):
        self.itens.append(item)

    @property
    def valor(self):
        return sum(map(lambda item: item.valor, self.itens))


def promocao_5_no_carrinho(carrinho: Carrinho):
    if len(carrinho.itens) >= 5:
        return carrinho.valor - (carrinho.valor * 0.1)


def promocao_mais_de_mill(carrinho: Carrinho):
    if carrinho.valor >= 1_000:
        return carrinho.valor - (carrinho.valor * 0.2)

def sem_promocao(carrinho: Carrinho):
    return carrinho.valor


class CalculadoraDePromocoes:
    def __init__(self, *promos: Callable):
        self.promos = promos
        self.fallback = sem_promocao

    def calcular(self, carrinho: Carrinho):
        for promo in self.promos:
            if (resultado := promo(carrinho)):
                return resultado

        return self.fallback(carrinho)


carrinho = Carrinho()
cp = CalculadoraDePromocoes(
    promocao_5_no_carrinho,
    promocao_mais_de_mill,
    sem_promocao
)

# carrinho.adicionar_item(Item(nome='Câmera', valor=1000))
carrinho.adicionar_item(Item(nome='Graveola', valor=1))

print(f'Valor sem promoção: {carrinho.valor}')
print(f'Valor com promoção: {cp.calcular(carrinho)}')
