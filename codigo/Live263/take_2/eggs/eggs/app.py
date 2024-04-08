from contextlib import asynccontextmanager
from datetime import datetime

from fastapi import Depends, FastAPI, Query
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .database import engine, get_session
from .models import Pessoa, reg


@asynccontextmanager
async def lifespan(app):
    async with engine.begin() as conn:
        await conn.run_sync(reg.metadata.drop_all)
        await conn.run_sync(reg.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)


class PessoaIn(BaseModel):
    username: str
    email: str
    senha: str


class PessoaOut(PessoaIn):
    id: int
    created_at: datetime


@app.get('/user/{user_id}', response_model=PessoaOut)
async def get_user(user_id: int, session: AsyncSession = Depends(get_session)):
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
    dump = pessoa.model_dump()
    pessoa_db = Pessoa(**dump)
    session.add(pessoa_db)
    await session.commit()

    await session.refresh(pessoa_db)

    return pessoa_db
