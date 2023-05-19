from typing import Optional
from sqlmodel import (
    Session, SQLModel, Field, create_engine, select,
    Relationship
)


class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    todos: list['Todo'] = Relationship()


class Todo(SQLModel, table=True):  # Tabela + JsonSchema
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    status: str = 'todo'

    person_id: int = Field(foreign_key='person.id')


engine = create_engine('sqlite:///db.db')
SQLModel.metadata.create_all(engine)

from pprint import pprint


with Session(engine) as session:
    query = select(Person).where(Person.id == 3)

    result = session.exec(query).first()

    print(result)

    pprint(result.todos)
