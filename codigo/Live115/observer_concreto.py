from observer_abc import Observador, Observavel

class BolaDeCristal:
    def atualizar(self, mensagem):
        print(f"Fausto está na escola, mas recebeu a mensagem: {mensagem}")

class Centauro:
    def __init__(self):
        self._observers = []

    def adicionar_observer(self, observador):
        self._observers.append(observador)

    def notificar_observers(self, mensagem):
        for observador in self._observers:
            observador.atualizar(mensagem)

class Unicornio:
    def __init__(self):
        self._observers = []

    def adicionar_observer(self, observador):
        self._observers.append(observador)

    def notificar_observers(self, mensagem):
        for observador in self._observers:
            observador.atualizar(mensagem)


unicornio = Unicornio()
unicornio.adicionar_observer(BolaDeCristal())
unicornio.notificar_observers('Os mortos chegaram #medo')


centauro = Centauro()
centauro.adicionar_observer(BolaDeCristal())
centauro.notificar_observers('Os mortos chegaram #medo')
