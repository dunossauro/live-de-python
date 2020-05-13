class Observavel:
    def __init__(self):
        self._observers = []

    def adicionar_observer(self, observador):
        self._observers.append(observador)

    def notificar_observers(self, mensagem):
        for observador in self._observers:
            observador(mensagem)


def observador_email(mensagem):
    print(f'observador_email recebeu a mensagem: {mensagem}')


def observador_impressora(mensagem):
    print(f'observador_impressora recebeu a mensagem: {mensagem}')


obs = Observavel()
obs.adicionar_observer(observador_email)
obs.adicionar_observer(observador_impressora)
obs.notificar_observers('A live de python é as 22')
