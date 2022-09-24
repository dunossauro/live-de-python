from typing import TypeVarTuple

Ts = TypeVarTuple('Ts')


def func(*args: *tuple[*Ts, bool]) -> tuple[int, *Ts, bool]:
    return 1, *args


reveal_type(func(1, 2, 3, 4, True))
