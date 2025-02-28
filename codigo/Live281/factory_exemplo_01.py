from dataclasses import dataclass
from datetime import date


@dataclass
class Pessoa:
    id: int
    username: str
    email: str
    criado_em: date
    amiges: 'Pessoa'


import factory


class PessoaFactory(factory.Factory):
    class Meta:
        model = Pessoa

    id = factory.Sequence(int)
    username = factory.Faker('user_name')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@test.com')
    criado_em = factory.LazyFunction(date.today)
    amiges = factory.SubFactory(PessoaFactory)
