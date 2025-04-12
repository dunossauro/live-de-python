from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, registry, Mapped, mapped_column, validates

# SQlalchemy configuration
engine = create_engine('sqlite:///database.db')

reg = registry()


@reg.mapped_as_dataclass
class Todo:
    __tablename__ = 'todos'

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)

    @validates('name')
    def validate_name(self, key, value):
        if not value:
            raise ValueError(f'{key} must be provider')
        return value


reg.metadata.create_all(engine)


def get_session():
    with Session(engine) as s:
        yield s


# Pydantic config
class TodoIn(BaseModel):
    name: str = Field(min_length=4)
    description: str


class TodoOut(TodoIn):
    id: int


# FastAPI configs
app = FastAPI()


@app.post('/create', response_model=TodoOut, status_code=201)
def create_todo(
    todo: TodoIn, session: Annotated[Session, Depends(get_session)]
):
    try:
        todo_db = Todo(**todo.model_dump())
        session.add(todo_db)
        session.commit()
        session.refresh(todo_db)

        return todo_db
    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code=400)
