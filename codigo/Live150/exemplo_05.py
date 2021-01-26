from typing import Dict


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, telefone: Dict[str, str], ddd: int):
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone
        self.ddd = ddd


eduardo_1 = Pessoa('Eduardo', 8, {'residencial': '1111-111', 'móvel': '999-999-999'}, 19)
eduardo_2 = Pessoa('Eduardo', 8, {'residencial': '1111-111', 'móvel': '999-999-999'}, 19)
