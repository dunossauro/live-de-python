from sqlmodel import Session, select
from sqlalchemy.orm import joinedload
from .models import Pessoa, Livro, engine


def create_livros(titulo: str, pessoa_id: int):
    livro = Livro(titulo=titulo, pessoa_id=pessoa_id)

    with Session(engine) as session:
        session.add(livro)
        session.commit()
        session.refresh(livro)

    return livro

def get_livros():
    query = select(Livro).options(joinedload('*'))
    with Session(engine) as session:
        result = session.execute(query).scalars().unique().all()

    return result


def create_pessoas(idade: int, nome: str):
    person = Pessoa(nome=nome, idade=idade)

    with Session(engine) as session:
        session.add(person)
        session.commit()
        session.refresh(person)

    return person

def get_pessoas(
    id: int = None,
    idade: int = None,
    limit: int = 5,
):
    query = select(Pessoa)

    if id:
        query = query.where(Pessoa.id == id)
    if idade:
        query = query.where(Pessoa.idade == idade)
    if limit:
        query = query.limit(limit)

    with Session(engine) as session:
        result = session.execute(query).scalars().all()

    return result
