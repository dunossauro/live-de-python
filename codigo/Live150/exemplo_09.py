from typing import Dict
from dataclasses import dataclass, field, InitVar


@dataclass
class Telefone:
    residencial: str
    movel: str


@dataclass(frozen=True)
class Pessoa:
    nome: str
    sobrenome: Dict[str, str]
    ddd: int = field(repr=False)
    telefone: InitVar[Telefone]

    def __post_init__(self, telefone):
        if self.telefone is None:
            self.telefone(*telefone)

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

eduardo_1 = Pessoa('Eduardo', 8, 19, ('1111-111', '999-999-999'))
#eduardo_2 = Pessoa('Eduardo', 8, {'residencial': '1111-111', 'móvel': '999-999-999'}, 19)
