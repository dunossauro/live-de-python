from typing import Final


class Pessoa:
    def __init__(self, nome) -> None:
        self.nome: Final = nome


p = Pessoa('Igor')
p.nome = 'Eduardo'
