from typing import Any, Dict, TypeVar

Number = TypeVar('Number', int, float, complex)

DadosDoCadastro = Dict[str, str]


def concatena(t1: Any, t2: Any)-> Any:
    return t1 + t2


def soma_numerica(x: Number, y: Number) -> Number:
    return x + y


def valida_cadastro(user: DadosDoCadastro) -> bool:
    ...
