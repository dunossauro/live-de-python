from typing import Dict


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, telefone: Dict[str, str], ddd: int):
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone
        self.ddd = ddd

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    def __eq__(self, other):
        return all([
            self.nome == other.nome,
            self.sobrenome == other.sobrenome,
            self.telefone == other.telefone,
            self.ddd == other.ddd
        ])

    def __repr__(self):
        return f'Pessoa({self.nome}, {self.sobrenome}, {self.telefone}, {self.ddd})'


eduardo_1 = Pessoa('Eduardo', 8, {'residencial': '1111-111', 'móvel': '999-999-999'}, 19)
eduardo_2 = Pessoa('Eduardo', 8, {'residencial': '1111-111', 'móvel': '999-999-999'}, 19)
