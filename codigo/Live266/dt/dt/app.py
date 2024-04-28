from contextlib import asynccontextmanager
from logging import DEBUG, getLogger
from datetime import datetime

from fastapi import Depends, FastAPI
from opentelemetry.trace import get_tracer
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import Task, engine, get_session, reg
from .tasks import relatorio

logger = getLogger()
logger.setLevel(DEBUG)

tracer = get_tracer('tracer')


class TaskSchemaIn(BaseModel):
    task_name: str
    task_name: str
    task_desc: str
    status: str = 'TODO'


class TaskSchemaOut(TaskSchemaIn):
    id: int
    created_at: datetime
    updated_at: datetime


@asynccontextmanager
async def lifespan(app):
    logger.info('Iniciando a aplicação na versão 1.1')
    reg.metadata.drop_all(engine)
    reg.metadata.create_all(engine)
    yield


app = FastAPI(lifespan=lifespan)


@app.get('/tasks', response_model=list[TaskSchemaOut])
def get_tasks():
    logger.info('listando tasks')
    with Session() as s:
        result = s.scalars(select(Task)).all()

        return result


@app.post('/tasks', response_model=TaskSchemaOut)
def create_task(task: TaskSchemaIn, session: Session = Depends(get_session)):
    logger.info('Criando task')
    with tracer.start_as_current_span(
        'Iniciando a criação da task', attributes=task.model_dump()
    ) as span:
        _task = Task(**task.model_dump())
        session.add(_task)
        session.commit()
        session.refresh(_task)

        span.add_event(
            'Registro inserido no banco de dados',
            attributes={'id': _task.id},
        )

        return _task


@app.post('/relatorio')
def background_task():
    result = relatorio.delay()

    return str(result)
