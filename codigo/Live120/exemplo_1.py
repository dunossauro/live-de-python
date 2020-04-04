class Lista:
    def __init__(self, elemento_0, elemento_1, elemento_2):
        self.lista = [elemento_0, elemento_1, elemento_2]

    def ordenar(self):
        return sorted(self.lista)

    def pegar_comeco(self):
        return self.lista[0]

    def __repr__(self):
        return str(self.lista)

class ListaInversivel(Lista)
    def ordenar(self):
        return list(reversed(sorted(self.lista)))


class ListaPega2Comeco(Lista):
    def pegar_comeco(self):
        return self.lista[:2]


class ListaIntInversivel(ListaInversivel):
    ...

class ListaStrInversivelPega2(ListaInversivel, ListaPega2Comeco):
    ...

class ListaListPega2(Lista, ListaPega2Comeco):
    ...
