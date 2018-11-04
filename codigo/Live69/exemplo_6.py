from abc import ABC, abstractmethod
from _collections_abc import _check_methods

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
    @classmethod
    def __subclasshook__(cls, classe):
        if cls is Fila:
            return _check_methods(
                classe,
                'entrar',
                'sair',
                '__len__',
                '__contains__',
                '__repr__'
            )
