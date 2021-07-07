from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    funcionaria: bool = False


def preço(pessoa: Pessoa, valor: int) -> str:
    match pessoa:
        case Pessoa('Eduardo'):
            return f'Assiste live de Python!'
        
        case Pessoa(nome, idade) if idade >= 65:
            return f'{nome.capitalize()} paga meia {valor/2}'

        case Pessoa(nome, _, True):
            return f'{nome.capitalize()} paga meia {valor/3}'

print(preço(
    Pessoa('Eduardo', 65, True), 20
))
