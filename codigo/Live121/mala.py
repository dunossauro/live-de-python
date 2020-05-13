from abc import ABC, abstractmethod

class Estado(ABC):
    @abstractmethod
    def em_evento(self, evento):
        ...

    def __repr__(self):
        return self.__class__.__name__


class EstadoFechado(Estado):
    def em_evento(self, evento: str, senha: str):
        evento, senha_passada = evento.split()
        if evento == 'abrir' and senha == senha_passada:
            return EstadoAberto()
        print('Mala Fechada, senha incorreta')
        return self


class EstadoAberto(Estado):
    def em_evento(self, evento: str, senha: str):
        if evento == 'fechar':
            return EstadoFechado()
        return self


class Mala:
    def __init__(self):
        self.senha = '0000'
        self.state = EstadoFechado()

    def __repr__(self):
        return f'Mala(estado={self.state})'

    def em_evento(self, evento: str):
        self.state = self.state.em_evento(
            evento, self.senha
        )
