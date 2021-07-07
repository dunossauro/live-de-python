class Pessoa:
    __match_args__ = 'nome', 'idade', 'funcionaria'

    def __init__(self, nome, idade, funcionaria=False):
        self.nome = nome
        self.idade = idade
        self.funcionaria = funcionaria

    def __repr__(self):
        return self.nome


def preço(pessoas: list[Pessoa]):
    match pessoas:
        case [
            Pessoa('Jarbas', jarbas_idade) as jarbas,
            Pessoa('Eduardo', eduardo_idade) as eduardo
        ]:
            return jarbas, jarbas_idade, eduardo, eduardo_idade

        case [(Pessoa('Jarbas') | Pessoa('Eduardo') as pessoa)]:
            return pessoa
        

print(preço(
    [Pessoa('Jarbas', 18, True), Pessoa('Eduardo', 18, True)]
))










