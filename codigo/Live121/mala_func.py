def em_evento_fechado(evento: str, senha: str):
    evento, senha_passada = evento.split()
    if evento == 'abrir' and senha == senha_passada:
        return 'aberto'
    print('Mala Fechada, senha incorreta')
    return 'fechado'


def em_evento_aberto(evento: str, senha: str):
    if evento == 'fechar':
        return 'fechado'
    return 'aberto'


def alternador_de_estados(estado):
    states = {
        'abrir': em_evento_aberto,
        'fechar': em_evento_fechado
    }
    return states[estado]



class Mala:
    def __init__(self):
        self.senha = '0000'
        self.state = alternador_de_estados('fechar')

    def __repr__(self):
        return f'Mala(estado={self.state})'

    def em_evento(self, evento: str):
        self.state = self.state(
            evento, self.senha
        )
