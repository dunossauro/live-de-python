class Bruxo:
    def bruxeis(self):
        print('The dead are coming back to life')


class Genio:
    def genieis(self):
        print('Los muertos vuelven a la vida')


class Deus:
    def deuseis(self):
        print('De doden komen weer tot leven')


class FalaAdapter:

    def __init__(self, ser, *, falar):
        self.ser = ser
        metodo_de_fala = getattr(self.ser, falar)
        self.__setattr__('falar', metodo_de_fala)


seres_adapters = [
    FalaAdapter(Bruxo(), falar='bruxeis'),
    FalaAdapter(Genio(), falar='genieis'),
    FalaAdapter(Deus(), falar='deuseis')
]

for adapter in seres_adapters:
    adapter.falar()
