from copy import copy
from datetime import datetime
from typing import Protocol


class Lembrança:
    def __init__(self, estado) -> None:
        self.estado = estado

    def get_estado(self):
        return self.estado


class Maldição(Protocol):
    """
    Maldição faz com que o almadiçoado tenha alguns comportamentos.
    """

    proibido: bool

    def acordar(self) -> Lembrança:
        ...

    def voltar_no_tempo(self, memento):
        ...


class Amaldiçoado:
    def __init__(self, nome):
        self.nome = nome
        self.proibido = False
        self.hora_atual = datetime.now()

    def ver_na_bola_de_cristal(self, algo):
        print(f'vendo {algo} na bola de cristal!')
        self.hora_atual = datetime.now()
        if algo == 'Diabão':
            self.proibido = True

    def acordar(self) -> Lembrança:
        state = copy(self.__dict__)
        return Lembrança(state)

    def voltar_no_tempo(self, memento):
        self.__dict__.clear()
        self.__dict__.update(memento.get_estado())

    def __repr__(self):
        return f'Amaldiçoado({self.__dict__})'


class Diabão:
    def __init__(self, amaldiçoado):
        self.amaldiçoado = amaldiçoado
        self.history = []

    def efetua_a_maldição(self):
        estado = self.amaldiçoado.acordar()
        self.history.append(estado)

    def voltar_no_tempo(self):
        estado = self.history.pop()
        self.amaldiçoado.voltar_no_tempo(estado)


fausto = Amaldiçoado('Fausto')
diabo = Diabão(amaldiçoado=fausto)
print(fausto)

fausto.acordar()
diabo.efetua_a_maldição()

from time import sleep

sleep(10)

fausto.ver_na_bola_de_cristal('zumbis')
print(fausto)

sleep(10)

fausto.ver_na_bola_de_cristal('Diabão')
diabo.voltar_no_tempo()
print(fausto)
