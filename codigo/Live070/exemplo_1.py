class Descritor:
    def __init__(self, obj):
        self.obj = obj

    def __set__(self, obj, val):
        print('Estou setando algo')
        self.obj = val

    def __get__(self, obj, tipo=None):
        print('Estou pegango algo')
        return self.obj

    def __delete__(self, obj):
        print('Estou deletando algo')
        del self.obj

    def __repr__(self):
        return self.obj


class MinhaClasse:
    batatinhas = Descritor('Bernardo Freitas')
