import logging
from datetime import datetime

import httpx
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class PessoaIn(BaseModel):
    username: str
    email: str
    senha: str


class PessoaOut(PessoaIn):
    id: int
    created_at: datetime


@app.get('/user/{user_id}')
async def get_user(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'http://eggs:8002/user/{user_id}')

        return response.json()


@app.get('/user')
async def get_users():
    async with httpx.AsyncClient() as client:
        response = await client.get('http://eggs:8002/user')

    return response.json()


@app.post('/user', response_model=PessoaOut)
async def create_user(user: PessoaIn):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            'http://eggs:8002/user', json=user.model_dump()
        )

        return response.json()
