from typing import Optional, List
import strawberry
from strawberry.fastapi import GraphQLRouter
from .db_function import (
    create_pessoas, get_pessoas, get_livros, create_livros
)


@strawberry.type
class Pessoa:
    id: Optional[int]
    nome: str
    idade: int
    livros: List['Livro']


@strawberry.type
class Livro:
    id: Optional[int]
    titulo: str
    pessoa: Pessoa


@strawberry.type
class Query:
    all_pessoa: List[Pessoa] = strawberry.field(resolver=get_pessoas)
    all_livro: List[Livro] = strawberry.field(resolver=get_livros)


@strawberry.type
class Mutation:
    create_pessoa: Pessoa = strawberry.field(resolver=create_pessoas)
    create_livro: Livro = strawberry.field(resolver=create_livros)


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)

graphql_app = GraphQLRouter(schema)
