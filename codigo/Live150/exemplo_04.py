from typing import NamedTuple, Dict


class Pessoa(NamedTuple):
    nome: str
    sobrenome: str
    telefone: Dict[str, str]
    ddd: int


eduardo_1 = Pessoa('Eduardo', 8, {'residencial': '1111-111', 'móvel': '999-999-999'}, 19)
eduardo_2 = Pessoa('Eduardo', 8, {'residencial': '1111-111', 'móvel': '999-999-999'}, 19)
