from abc import ABC, abstractmethod

class Fila(ABC):
    @abstractmethod
    def __init__(self, iterável):
        self.it = []

    @abstractmethod
    def entrar(self, obj):
        ...
    @abstractmethod
    def sair(self, pos=0):
        ...
    @abstractmethod
    def __len__(self):
        ...

    @abstractmethod
    def __contains__(self, obj):
        ...

    @abstractmethod
    def __repr__(self):
        ...
