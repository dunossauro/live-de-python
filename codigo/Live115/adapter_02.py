class Bruxo:
    def bruxeis(self):
        print('The dead are coming back to life')


class Genio:
    def genieis(self):
        print('Los muertos vuelven a la vida')


class Deus:
    def deuseis(self):
        print('De doden komen weer tot leven')


class BruxoAdapter:
    def __init__(self, bruxo):
        self.bruxo = bruxo

    def falar(self):
        self.bruxo.bruxeis()


class GenioAdapter:
    def __init__(self, genio):
        self.genio = genio

    def falar(self):
        self.genio.genieis()


class DeusAdapter:
    def __init__(self, deus):
        self.deus = deus

    def falar(self):
        self.deus.deuseis()


seres = [
    BruxoAdapter(Bruxo()),
    GenioAdapter(Genio()),
    DeusAdapter(Deus())
]

for ser in seres:
    ser.falar()
