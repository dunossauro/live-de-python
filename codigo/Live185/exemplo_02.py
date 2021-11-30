from typing import Optional
import strawberry
from sqlmodel import (
    SQLModel,
    Field,
    create_engine,
    select,
    Session
)

# Criar engine do banco
engine = create_engine('sqlite:///database.db')


class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    idade: int


# Cria o banco de dados
SQLModel.metadata.create_all(engine)

def create_app(idade: int, nome: str):
    person = Person(nome=nome, idade=idade)

    with Session(engine) as session:
        session.add(person)
        session.commit()
        session.refresh(person)

    return person
   


@strawberry.type
class Pessoa:
    id: Optional[int]
    nome: str
    idade: int


@strawberry.type
class Query:

    @strawberry.field
    def all_pessoa(self) -> list[Pessoa]:
        query = select(Person)
        with Session(engine) as session:
            result = session.execute(query).scalars().all()

        return result

@strawberry.type
class Mutation:
    create_pessoa: Pessoa = strawberry.field(resolver=create_app)


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)
