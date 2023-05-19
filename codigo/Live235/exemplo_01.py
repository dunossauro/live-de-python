from typing import Optional
from sqlmodel import (
    Session, SQLModel, Field, create_engine, select,
)


class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class Todo(SQLModel, table=True):  # Tabela + JsonSchema
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    status: str = 'todo'

    person_id: int = Field(foreign_key='person.id')


engine = create_engine('sqlite:///db.db')
SQLModel.metadata.create_all(engine)

"""
Métodos do exec:

- all: pega todos
- one: pega um
- first: pega o primeiro
- partitions: particiona a resposta
"""

from pprint import pprint


with Session(engine) as session:
    query = (
        select(Todo)
        .where(Todo.person_id == 2)
        # .limit(20)
        # .order_by(Todo.title)
        # .join(Person)
        # .offset(12)
    )

    pprint(
        session.exec(query).all()
    )
