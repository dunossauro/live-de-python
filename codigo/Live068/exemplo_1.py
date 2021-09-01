"""Implementar um Container."""
from collections.abc import Container, Sized, Collection

class Caixa(Collection):
    def __init__(self, seq):
        self.seq = seq

    def __contains__(self, outro):
        return outro in list(self.seq)

    def __len__(self):
        return len(self.seq)

    def __iter__(self):
        return self


class MyList(List):
    ...
