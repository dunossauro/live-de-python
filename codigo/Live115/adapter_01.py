class Bruxo:
    def bruxeis(self):
        print('The dead are coming back to life')


class Genio:
    def genieis(self):
        print('Los muertos vuelven a la vida')


class Deus:
    def deuseis(self):
        print('De doden komen weer tot leven')


seres = [Bruxo(), Genio(), Deus()]

for ser in seres:
    if isinstance(ser, Bruxo):
        ser.bruxes()
    elif isinstance(ser, Genio):
        ser.genies()
    else:
        ser.deuses()
