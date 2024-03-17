from contextlib import asynccontextmanager
from datetime import datetime
from typing import Annotated

from fastapi import Depends, FastAPI, Query
from opentelemetry import trace
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .database import engine, get_session
from .mid import MetricsMeddleware
from .models import Pessoa, reg

SQLAlchemyInstrumentor().instrument(engine=engine.sync_engine)

tracer = trace.get_tracer('eggs.tracer')


@asynccontextmanager
async def lifespan(app):
    with tracer.start_as_current_span('A magia do banco de dados!'):
        async with engine.begin() as conn:
            await conn.run_sync(reg.metadata.drop_all)
            await conn.run_sync(reg.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)
app.add_middleware(MetricsMeddleware)


class PessoaIn(BaseModel):
    username: str
    email: str
    senha: str


class PessoaOut(PessoaIn):
    id: int
    created_at: datetime


@app.get('/user/{user_id}', response_model=PessoaOut)
async def get_user(user_id: int, session: AsyncSession = Depends(get_session)):
    with tracer.start_as_current_span(f'Buscando {user_id=} no banco'):
        result = await session.get(Pessoa, user_id)
        return result


@app.get('/user', response_model=list[PessoaOut])
async def get_users(
    limit: int = Query(default=50),
    offset: int = Query(default=0),
    session: AsyncSession = Depends(get_session),
):
    result = await session.scalars(select(Pessoa).limit(limit).offset(offset))
    return result.all()


@app.post('/user', response_model=PessoaOut)
async def create_user(
    pessoa: PessoaIn, session: AsyncSession = Depends(get_session)
):
    with tracer.start_as_current_span('Inserindo user no banco') as s:
        dump = pessoa.model_dump()
        s.add_event('dados recebidos', dump)
        pessoa_db = Pessoa(**dump)
        session.add(pessoa_db)
        await session.commit()

    with tracer.start_as_current_span('Refresh no banco'):
        await session.refresh(pessoa_db)

    return pessoa_db
