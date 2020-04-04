from abc import ABC, abstractmethod

class Ordenavel(ABC):
    @abstractmethod
    def ordenar(self):
        ...

class OrdenavelReversa(Ordenavel):
    def ordenar(self):
        return list(reversed(sorted(self.lista)))

class OrdenavelSimples(Ordenavel):
    def ordenar(self):
        return sorted(self.lista)


class PegaComeco(ABC):
    @abstractmethod
    def pegar_comeco(self):
        ...

class PegarComeco1(PegaComeco):
    def pegar_comeco(self):
        return self.list[0]

class PegarComecoAte3(PegaComeco):
    def pegar_comeco(self):
        return self.list[:3]



class Lista:
    def __init__(
        self, elemento_0, elemento_1, elemento_2
        i_ordernar, i_pegar_comeco,
    ):
        self.lista = [elemento_0, elemento_1, elemento_2]
        self.i_ordernar = i_ordernar
        self.i_pegar_comeco = i_pegar_comeco

    def ordenar(self):
        return self.i_ordernar(self)

    def pegar_comeco(self):
        return i_pegar_comeco(self)

    def __repr__(self):
        return str(self.lista)



lista_int_inversivel = Lista(
    0, 1, 2,
    OrdenavelReversa(),
    PegarComeco() or PegarComecoAte3()
)

ListaStrInversivelPegaAte3 = Lista(
    0, 1, 2,
    OrdenavelReversa(),
    PegarComecoAte3()
)


ListaListPegaAte3 = Lista(
    0, 1, 2,
    OrdenavelReversa(),
    PegarComecoAte3()
)
