from typing import Callable, TypeVar, Generator

T = TypeVar('T')

a = [1, 10]
b = ['a', 'eduardo']


def menor_5(val: int) -> bool:
    return val < 5


def tam_menor_5(val: str) -> bool:
    return len(val) < 5


def meu_filtro(
    func: Callable[[T], bool], vals: list[T]
) -> Generator[T, None, None]:
    for val in vals:
        if func(val):
            yield val


print(list(meu_filtro(menor_5, a)))
print(list(meu_filtro(tam_menor_5, b)))
