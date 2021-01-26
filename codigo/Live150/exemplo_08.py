from typing import Dict
from dataclasses import dataclass, field


def xpto():
    ...


@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    ddd: int = field(repr=False)
    telefone: Dict[str, str] = field(default_factory=dict)
    nome_completo: str = field(init=False)

    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'


eduardo_1 = Pessoa('Eduardo', '', {'residencial': '1111-111', 'móvel': '999-999-999'}, 19)
eduardo_2 = Pessoa(
    'Eduardo', 8, {'residencial': '1111-111', 'móvel': '999-999-999'}, 19
)
