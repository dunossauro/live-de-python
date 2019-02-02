"""Se conta como uma sequência e tem itens como sequencia.

Então, é uma sequencia."""
from collections.abc import Sequence

class MinhaTupla(Sequence):
    def __init__(self, *vals):
        self.vals = vals

    def __getitem__(self, pos):
        return self.vals[pos]

    def __len__(self):
        return len(self.vals)
