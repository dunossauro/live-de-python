from typing import Dict
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    telefone: Dict[str, str]
    ddd: int


@dataclass(repr=False, frozen=True)
class Pessoa:
    nome: str
    sobrenome: str
    telefone: Dict[str, str]
    ddd: int
    nome_completo: str = None

    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'

eduardo_1 = Pessoa('Eduardo', 8, {'residencial': '1111-111', 'móvel': '999-999-999'}, 19)
eduardo_2 = Pessoa('Eduardo', 8, {'residencial': '1111-111', 'móvel': '999-999-999'}, 19)
