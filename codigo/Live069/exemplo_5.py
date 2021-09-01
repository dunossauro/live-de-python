from exemplo_6 import Fila

class Banheiro:
    def __init__(self):
        self.it = []

    def entrar(self, obj):
        self.it.append(obj)

    def sair(self, pos=0):
        return self.it.pop(pos)

    def __len__(self):
        return len(self.it)

    def __contains__(self, obj):
        return obj in self.it

    def __repr__(self):
        return f'Fila({self.it})'
