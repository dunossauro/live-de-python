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

# Usando ID Fixo


def create_tasks(title: str, status: str = 'todo'):
    with Session(engine) as session:
        session.add(
            Todo(title=title, status=status, person_id=1)
        )
        session.commit()


def read_tasks(person_id: int):
    with Session(engine) as session:
        person = session.get(Person, person_id)

        return person.todos


def update_tasks(
    task_id: int, task_title: str = None, task_status: str = None
):
    with Session(engine) as session:
        task = session.get(Todo, task_id)
        if task_title:
            task.title = task_title
        if task_status:
            task.status = task_status

        session.commit()

def delete_tasks(task_id: int):
    with Session(engine) as session:
        task = session.get(Todo, task_id)
        session.delete(task)
        session.commit()
