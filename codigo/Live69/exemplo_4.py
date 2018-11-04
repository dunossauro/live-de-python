from collections import namedtuple
from exemplo_3 import Fila

pessoa = namedtuple('Pessoa', 'nome idade gestante deficiente')


class Padaria(Fila):
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


class Supermercado(Fila):
    def __init__(self):
        self.it = []
        self.pri = []

    def entrar(self, obj):
        if isinstance(obj, pessoa):
            if obj.gestante or obj.deficiente or obj.idade > 64:
                self.pri.append(obj)
            else:
                self.it.append(obj)
        else:
            raise NotImplementedError

    def sair(self, pos=0):
        if self.pri:
            return self.pri.pop(pos)
        return self.it.pop(pos)

    def __len__(self):
        return len(self.it) + len(self.pri)

    def __contains__(self, obj):
        return obj in self.it or obj in self.pri

    def __repr__(self):
        return f'Fila({self.pri + self.it})'
