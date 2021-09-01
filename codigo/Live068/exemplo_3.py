"""Se conta como uma sequência e tem itens como sequencia.

Então, é uma sequencia."""
from collections.abc import MutableSequence

class MinhaLista(MutableSequence):
    def __init__(self, *vals):
        self.vals = vals

    def __getitem__(self, pos):
        return self.vals[pos]

    def __len__(self):
        return len(self.vals)

    def __delitem__(self, item):
        del self.vals[item]

    def __setitem__(self, pos, valor):
        self.vals[pos] = valor
