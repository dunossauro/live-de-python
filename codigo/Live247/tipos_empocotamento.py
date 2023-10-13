from typing import (
    TypedDict, Unpack, Required, NotRequired
)


class ArgumentosNomeados(TypedDict):
    nome: Required[str]
    live: NotRequired[list[int]]


def xpto(
    *args: int | float,
    **kwargs: Unpack[ArgumentosNomeados],
):
    print(args)
    print(kwargs)



xpto(
    1, 2, 3, 4, 5, 6, 7,
    nome='batata',
    # live='de python'.split(),
)
