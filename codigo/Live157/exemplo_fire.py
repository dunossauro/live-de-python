import fire

meu_dicionario = {
    'nome': 'Eduardo',
    'hobbies': ['toicar violão', 'Fazer lives', 'andar de skate'],
    'aniversario': {
        'dia': 6,
        'mes': 3
    }
}


def olar(nome='bb'):
    """Diz olá para o bb!"""
    return f'Olar {nome}!'


def batatinha():
    return 42


class Grupo:
    def batata(self, num):
        return f'Tenho {num} de batatas'


fire.Fire()
