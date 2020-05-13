from abc import ABC, abstractmethod, abstractproperty
from typing import List

class Observador(ABC):
    """Feitiço para objetos que querem ser observados."""

    @abstractmethod
    def atualizar(self):
        ...


class Observavel(ABC):
    """Feitiço observar objetos observáveis."""

    @property
    @abstractmethod
    def observers() -> List:
        ...

    @abstractmethod
    def adicionar_observer(self, observer):
        ...

    @abstractmethod
    def notificar_observers(self, mensagem):
        ...
