from typing import runtime_checkable, Protocol


@runtime_checkable
class FazBusca(Protocol):
    def busca(self, val):
        ...


class SubTipo:
    ...

t = SubTipo()

print(isinstance(t, FazBusca))  #  False

t.busca = lambda self, val: self.xpto(val)

print(isinstance(t, FazBusca))  #  False
