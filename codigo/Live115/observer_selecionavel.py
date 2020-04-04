class BolaDeCristal:
    def atualizar(self, mensagem):
        print(f"Fausto está na escola, mas recebeu a mensagem: {mensagem}")

class Unicornio:
    def __init__(self, nome):
        self.nome = nome

    def atualizar(self, mensagem):
        print(f"{self.nome} recebeu '{mensagem}'")


class NotificacoesUnicornences:
    def __init__(self, tipos):
        self._observers = {tipo: [] for tipo in tipos}

    def adicionar_observer(self, tipo, pessoa):
        self._observers[tipo].append(pessoa)

    def notificar_observers(self, tipo, message):
        for subscriber in self._observers[tipo]:
            subscriber.atualizar(message)


pub = NotificacoesUnicornences(['comida', 'musica', 'mortos'])

pub.adicionar_observer('comida', Unicornio('Geraldo'))
pub.adicionar_observer('musica', Unicornio('Geraldo'))
pub.adicionar_observer('mortos', Unicornio('Geraldo'))
pub.adicionar_observer('mortos', BolaDeCristal())

pub.notificar_observers('comida', 'Hora do rango')
pub.notificar_observers('mortos', 'Os mortos voltaram')
