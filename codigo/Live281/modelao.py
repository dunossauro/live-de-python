from dataclasses import dataclass
from datetime import date, datetime

@dataclass
class Endereco:
    rua: str
    numero: str
    bairro: str
    cidade: str
    estado: str
    cep: str
    pais: str


@dataclass
class Usuario:
    id: int
    nome: str
    sobrenome: str
    email: str
    senha: str
    telefone: str
    data_nascimento: date
    cpf: str
    rg: str
    endereco: Endereco
    data_registro: datetime
    ultimo_acesso: datetime
    ativo: bool
    nivel_acesso: str = 'usuario'
    foto_perfil: str | None = None


## Exemplo de uso

usuario_exemplo = Usuario(
    id=1,
    nome="João",
    sobrenome="Silva",
    email="joao.silva@email.com",
    senha="senha_segura_123",
    telefone="(11) 98765-4321",
    data_nascimento=date(1990, 5, 23),
    cpf="123.456.789-00",
    rg="12.345.678-9",
    endereco=Endereco(
        rua="Rua Fictícia",
        numero="123",
        bairro="Centro",
        cidade="Cidade Exemplo",
        estado="EX",
        cep="12345-678",
        pais="País Exemplo"
    ),
    data_registro=datetime.now(),
    ultimo_acesso=datetime.now(),
    ativo=True,
    nivel_acesso="usuario",
    foto_perfil="http://exemplo.com/foto.jpg"
)


import factory

class EnderecoFactory(factory.Factory):
    class Meta:
        model = Endereco

    rua = factory.Faker('street_name')
    numero = factory.Faker('building_number')
    bairro = factory.Faker('bairro', locale='pt_BR')
    cidade = factory.Faker('city')
    estado = factory.Faker('state_abbr')
    cep = factory.Faker('zipcode')
    pais = factory.Faker('country')


class UserFactory(factory.Factory):
    class Meta:
        model = Usuario

    nome = factory.Faker('name')
    sobrenome = factory.Faker('last_name')
    email = factory.Faker('email')
    senha = factory.Faker('password')
    telefone = factory.Faker('phone_number')
    data_nascimento = factory.Faker('date')
    data_registro = factory.Faker('date')
    ultimo_acesso = factory.Faker('date')
    rg = factory.Faker('rg', locale='pt_BR')
    cpf = factory.Faker('cpf', locale='pt_BR')
    ativo = factory.Faker('pybool')
    id = factory.Sequence(int)
    endereco = factory.SubFactory(Faker('pylist', type=EnderecoFactory))


class UserAtivoFactory(UserFactory):
    ativo = True


def test_com_faker(faker: Faker):
    fake_data = {
        'name': faker.name()
    }
