from abc import ABC, abstractmethod


class Notificado(ABC):
    """Interface para objetos que querem ser notificados."""
    @abstractmethod
    def atualizar(self):
        ...

class Bruxo:
    def atualizar(self, msg):
        print(f'Bruxos receberam: {msg}')


class Genio:
    def atualizar(self, msg):
        print(f'Gênios receberam: {msg}')


class Deus:
    def atualizar(self, msg):
        print(f'Deuses receberam: {msg}')


class GerenciadorDeNotificacoes:
    def __init__(self):
        self._seres = []

    def acrecentar_ser(self, ser):
        self._seres.append(ser)

    def notificar_seres(self, data):
        for ser in self._seres:
            ser.atualizar(data)


notificacoes = GerenciadorDeNotificacoes()

notificacoes.acrecentar_ser(Deus())
notificacoes.acrecentar_ser(Genio())
notificacoes.acrecentar_ser(Bruxo())

notificacoes.notificar_seres('Os mortos chegaram aaaaaaaaaaaaaaaaaaa')
