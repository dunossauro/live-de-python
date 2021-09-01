class Descritor:
    def __init__(self, obj):
        self.obj = obj

    def __set__(self, obj, val):
        print('Estou setando algo')
        self.obj = val

    def __get__(self, obj, tipo=None):
        print('Estou pegango algo')
        return self.obj

    def __repr__(self):
        return self.obj

class Cliente:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nome_completo = f'{self.nome} {self.sobrenome}'
