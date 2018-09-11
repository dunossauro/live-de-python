class Pizzaria:
    def __init__(self):
        self._pizzaolo = Pizzaolo()

    def pedido(self, pizza):
        self._pizzaolo.preparar_pizza(pizza)

class Forno:
    def __init__(self):
        self.pizzas = []
        self.lenha = None

    def assar(self, pizza):
        if not self.lenha:
            print('Não há lenha')

class Pizzaolo:
    def __init__(self):
        self._forno = Forno()

    def preparar_pizza(self, pizza):
        self._forno.assar(pizza)
