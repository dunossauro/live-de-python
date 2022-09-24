from typing import TypedDict, NotRequired, Required, Self


class Iterable:
    def __iter__(self) -> Self:
        return self


class Pessoa(TypedDict, total=False):
    nome: Required[str]
    idade: Required[int]
    peso: float


d: Pessoa = {
    'nome': 'Eduardo', 'idade': 18
}

d2: Pessoa = {
    'nome': 'Eduardo', 'idade': 18, 'peso': 50.00
}
