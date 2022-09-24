from typing import TypeVarTuple, Unpack

Ts = TypeVarTuple('Ts')


# compatível
def func(
    *args: Unpack[tuple[Unpack[Ts], bool]],
) -> tuple[Unpack[Ts]]:
    return args[:-1]


# 3.11 +
def func(
    *args: *tuple[*Ts, bool],
) -> tuple[*Ts]:
    return args[:-1]


func(1, 2, 3, 4, True)
