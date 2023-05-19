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

from fastapi import FastAPI

app = FastAPI()

@app.post('/task', response_model=Todo)
def create_tasks(todo: Todo) -> Todo:
    with Session(engine) as session:
        session.add(todo)
        session.commit()
        session.refresh(todo)

        return todo

@app.get('/task', response_model=list[Todo])
def read_tasks(person_id: int) -> list[Todo]:
    with Session(engine) as session:
        person = session.get(Person, person_id)

        return person.todos

@app.patch('/task', response_model=Todo)
def update_tasks(task_id: int, task_update: Todo) -> Todo:
    with Session(engine) as session:
        task = session.get(Todo, task_id)
        task.title = task_update.title
        task.status = task_update.status

        session.commit()

@app.delete('/task', response_model=Todo)
def delete_tasks(task_id: int) -> Todo:
    with Session(engine) as session:
        task = session.get(Todo, task_id)
        session.delete(task)
        session.commit()

        return task
