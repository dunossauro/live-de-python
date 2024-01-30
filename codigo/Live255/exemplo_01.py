from datetime import datetime
from typing import Protocol

from rich import print


class Lembrança:
    def __init__(self, memoria) -> None:
        self.memoria = memoria

    def pega_memoria(self):
        return self.memoria

    def __repr__(self) -> str:
        return f'Lembrança({self.memoria})'


class Maldição(Protocol):
    """Maldição do tempo e das lembranças."""
    proibido: bool

    def gerar_lembrança(self):
        ...

    def implanta_a_lembrança(self, lembrança):
        ...


class Pessoa:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.proibido = False
        self.ultima_lembrança = datetime.now()

    def olhar_bola_de_cristal(self, alguem):
        if alguem == 'Diabão':
            self.proibido = True
        self.ultima_lembrança = datetime.now()

    def gerar_lembrança(self):
        return Lembrança(self.__dict__.copy())

    def implanta_a_lembrança(self, lembrança):
        self.__dict__.clear()
        self.__dict__.update(lembrança.memoria)


class Diabão:
    def __init__(self, amaldiçoado) -> None:
        self.amaldiçoado = amaldiçoado
        self.historico = []

    def efetua_a_maldição(self):
        print('Diabão acinou a maldição!')
        lambrança = self.amaldiçoado.gerar_lembrança()
        self.historico.append(lambrança)

    def volta_no_tempo(self):
        lembrança = self.historico.pop()
        self.amaldiçoado.implanta_a_lembrança(lembrança)


fausto = Pessoa(nome='Fausto')

diabo = Diabão(fausto)
diabo.efetua_a_maldição()
print(diabo.historico)

from time import sleep

sleep(2)

fausto.olhar_bola_de_cristal('Apst L')
diabo.efetua_a_maldição()
print(diabo.historico)


sleep(2)

fausto.olhar_bola_de_cristal('Diabão')
print(diabo.historico)

if fausto.proibido:
    diabo.volta_no_tempo()

print(diabo.historico)
