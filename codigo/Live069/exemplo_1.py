from abc import ABC, abstractmethod


class MinhaABC(ABC):

    @abstractmethod
    def meu_metodo_de_exemplo(self):
        ...

    @classmethod
    @abstractmethod
    def meu_metodo_de_classe(self):
        ...

    @staticmethod
    @abstractmethod
    def meu_metodo_estático(self):
        ...

    @abstractmethod
    def meu_metodo_estático(self):
        ...
