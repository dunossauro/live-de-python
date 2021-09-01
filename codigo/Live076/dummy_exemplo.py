"""Exemplo do dublê Dummy usando typing."""
from typing import NewType, Any

Dummy = NewType('Dummy', Any)

class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


Pessoa('Eduardo', 'Mendes', Dummy(25))
