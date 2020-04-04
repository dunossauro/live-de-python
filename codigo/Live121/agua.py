from abc import ABC, abstractmethod

class Estado(ABC):
    @abstractmethod
    def esquentar(self):
        ...

    @abstractmethod
    def esfriar(self):
        ...

    def __repr__(self):
        return self.__class__.__name__


class EstadoSolido(Estado):
    def esquentar(self):
        return EstadoLiquido()

    def esfriar(self):
        return EstadoSolido()


class EstadoLiquido(Estado):
    def esquentar(self):
        return EstadoGasoso()

    def esfriar(self):
        return EstadoSolido()


class EstadoGasoso(Estado):
    def esquentar(self):
        # raise Exception('Não dá mais. Já tá quente')
        return EstadoGasoso()

    def esfriar(self):
        return EstadoLiquido()


class Elemento:
    def esquentar(self):
        self.state = self.state.esquentar()

    def esfriar(self):
        self.state = self.state.esfriar()

    def __repr__(self):
        return f'{self.nome}(estado={self.state})'


class Mercurio(Elemento):
    def __init__(self):
        self.nome = 'Mercurio'
        self.state = EstadoLiquido()


class Agua(Elemento):
    def __init__(self):
        self.nome = 'Agua'
        self.state = EstadoLiquido()
