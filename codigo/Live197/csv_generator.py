from csv import writer
from dataclasses import dataclass
from datetime import date, timedelta
from itertools import count
from random import randint

from factory import Factory, Faker, LazyAttribute, LazyFunction, Sequence
from factory.fuzzy import FuzzyChoice
from faker import Faker as FFaker

c_date = count(1)
c_email = count(1)
fake = FFaker('pt_BR')
Faker._DEFAULT_LOCALE = 'pt_BR'


# TODO: Criar caso onde a data errada vai bater com pagamento pendente


def randon_date_factor():
    randon_factor = next(c_date)
    if randon_factor % 101 == 0:
        return ''

    if randon_factor % 56 == 0:
        return date(2027, 12, 31)

    return fake.date_between(
        date.today() + timedelta(-(randint(1, 30))),
        date.today()
    )


def randon_email_factor(obj):
    if next(c_email) % 203 == 0:
        return ''

    name = obj.first_name.replace(' ', '_')
    last = obj.last_name.replace(' ', '_')

    result = f'{name}_{last}'.lower()
    return result + '@' + fake.ascii_email().split('@')[-1]


@dataclass
class Data:
    _id: int
    first_name: str
    last_name: str
    email: str
    ultimo_pagamento: date
    status: str
    pagamento: str


class DataFactory(Factory):
    class Meta:
        model = Data

    _id = Sequence(lambda n: n)
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    email = LazyAttribute(randon_email_factor)
    ultimo_pagamento = LazyFunction(randon_date_factor)
    status = FuzzyChoice(['ativo', 'inativo'] * 100 + [''])
    pagamento = FuzzyChoice(['em dia', 'inadinplente'] * 100 + [''])


fields = Data.__match_args__
rows = [DataFactory().__dict__.values() for x in range(10_000)]


with open('dados.csv', 'w') as csvfile:
    csvwriter = writer(csvfile)
    csvwriter.writerow(fields)

    csvwriter.writerows(rows)
