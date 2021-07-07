class Pessoa:
    __match_args__ = 'nome', 'idade', 'funcionaria'

    def __init__(self, nome, idade, funcionaria=False):
        self.nome = nome
        self.idade = idade
        self.funcionaria = funcionaria


def preço(pessoa: Pessoa, valor: int) -> str:
    match pessoa:
        case Pessoa('Eduardo' | 'Jarbas'):
            return f'Assiste live de Python!'
        
        case Pessoa(nome, idade) if idade >= 65:
            return f'{nome.capitalize()} paga meia {valor/2}'

        case Pessoa(nome, _, True):
            return f'{nome.capitalize()} paga meia {valor/3}'

print(preço(
    Pessoa('Jarbas', 18, True), 20
))
