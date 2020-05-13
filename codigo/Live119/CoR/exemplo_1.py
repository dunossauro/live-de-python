from abc import ABC, abstractmethod

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


class Promocao(ABC):

    # @abstractproperty
    # def next(self):
    #     ...

    @abstractmethod
    def calcular(self, valor):
        ...


class Promocao5NoCarrinho(Promocao):
    def __init__(self, next=None):
        self.next = next

    def calcular(self, carrinho: Carrinho):
        if len(carrinho.itens) >= 5:
            return carrinho.valor - (carrinho.valor * 0.1)

        return self.next.calcular(carrinho)


class PromocaoMaisDeMil(Promocao):
    def __init__(self, next=None):
        self.next = next

    def calcular(self, carrinho: Carrinho):
        if carrinho.valor >= 1_000:
            return carrinho.valor - (carrinho.valor * 0.2)

        return self.next.calcular(carrinho)

class SemPromocao(Promocao):
    def calcular(self, carrinho: Carrinho):
        return carrinho.valor


class CalculadoraDePromocoes:
    def calcular(self, valor):
        p1 = PromocaoMaisDeMil()
        p2 = Promocao5NoCarrinho()
        p3 = SemPromocao()

        p1.next = p2
        p2.next = p3

        return p1.calcular(valor)

        # return PromocaoMaisDeMil(
        #     next=Promocao5NoCarrinho(next=SemPromocao())
        # ).calcular(valor)


# class CalculadoraDePromocoesSemPatter:
#     def calcular(self, carrinho: Carrinho):
#         if carrinho.valor >= 1_000:
#             ...
#         if len(carrinho.itens):
#             ...
#         if ():
#             ...
#


carrinho = Carrinho()

# carrinho.adicionar_item(Item(nome='Fritas', valor=8))
# carrinho.adicionar_item(Item(nome='Fritas', valor=8))
# carrinho.adicionar_item(Item(nome='Fritas', valor=8))
# carrinho.adicionar_item(Item(nome='Fritas', valor=8))
# carrinho.adicionar_item(Item(nome='Fritas', valor=8))
# carrinho.adicionar_item(Item(nome='Câmera', valor=1000))
carrinho.adicionar_item(Item(nome='Câmera', valor=1000))
carrinho.adicionar_item(Item(nome='Graveola', valor=1))


cp = CalculadoraDePromocoes()

print(f'Valor sem promoção: {carrinho.valor}')
print(f'Valor com promoção: {cp.calcular(carrinho)}')
