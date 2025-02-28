from dataclasses import dataclass
from datetime import date


@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    cpf: str
    data_de_nascimento: date


from factory import Factory, Faker


class PessoaFactory(Factory):
    class Meta:
        model = Pessoa

    nome = Faker('first_name', locale='pt_BR')
    sobrenome = Faker('last_name', locale='pt_BR')
    cpf = Faker('cpf', locale='pt_BR')
    data_de_nascimento = Faker('date_object')

