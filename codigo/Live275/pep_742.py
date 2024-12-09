"""
Para especificar o comportamento do `TypeIs`,
vamos usar a seguinte terminologia:
- I = TypeIs de entrada
- R = TypeIs tipo de retorno
- A = Tipo do argumento que será passado para o afunilamento
- AP = Afunilamento positivo; usando quando TypeIs retorna True
- AN = Afunilamento negativo; usando quando TypeIs retorna False
"""

from typing import TypeIs


def is_int(
    argunto_de_entrada: int | str  # I
) -> TypeIs[int]:  # R
    return isinstance(argunto_de_entrada, int)


def vai_ser_afunilada(
    argumento: str | int  # A
):
    if is_int(argumento):  # AP
        reveal_type(argumento)
    else:  # AN
        reveal_type(argumento)


from typing import TypeGuard

def is_int(x) -> TypeGuard[int]:
    return isinstance(x, int)
