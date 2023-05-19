from typing import Optional
from sqlmodel import (
    Session, SQLModel, Field, create_engine, select,
    Relationship
)


class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    todos: Optional[list['Todo']] = Relationship(back_populates='person')


class Todo(SQLModel, table=True):  # Tabela + JsonSchema
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    status: str = 'todo'

    person_id: int = Field(foreign_key='person.id')
    person: Optional['Person'] = Relationship(back_populates='todos')


engine = create_engine('sqlite:///db.db')
SQLModel.metadata.create_all(engine)

from pprint import pprint


with Session(engine) as session:
    session.add(
        Person(
            name='Regy',
            todos=[
                Todo(title='Comer'),
                Todo(title='Dormir'),
                Todo(title='Amar'),
                Todo(title='sair'),
            ]
        )
    )
    session.commit()

    query = select(Person).where(Person.name == 'Regy')

    regy = session.exec(query).first()

    print(regy)
    pprint(regy.todos)
