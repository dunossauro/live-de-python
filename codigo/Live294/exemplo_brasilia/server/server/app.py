from datetime import datetime
from enum import Enum

from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, ConfigDict
from redis import Redis
from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import Mapped, Session, registry, mapped_column
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str


class _Status(str, Enum):
    checkout = 'checkout'
    estoque = 'estoque'
    pagamento = 'pagamento'
    envio = 'envio'
    nota = 'nota'
    erro = 'erro'


engine = create_engine(Settings().DATABASE_URL)
reg = registry()


@reg.mapped_as_dataclass
class Status:
    __tablename__ = 'status'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)

    c_id: Mapped[int]
    status: Mapped[_Status]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )


class Produto(BaseModel):
    p_id: int
    c_id: int


class Message(BaseModel):
    content: str

class SStatus(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    c_id: int
    status: str
    created_at: datetime


class StatusList(BaseModel):
    statuses: list[SStatus]


app = FastAPI()
app.mount(
    '/static',
    StaticFiles(directory='static'),
    name='static'
    
)
templates = Jinja2Templates('templates')
redis = Redis(host=Settings().REDIS_URL)


@app.get('/', response_class=HTMLResponse)
def produtos(request: Request):
    return templates.TemplateResponse(
        request=request, name='index.html'
    )


@app.post('/compra', response_model=Message, status_code=201)
def comprar(produto: Produto):
    redis.publish(
        'checkout', produto.model_dump_json()
    )
    return {'content': 'Compra em andamento!'}


def get_session():
    with Session(engine) as s:
        yield s


@app.get('/status/{c_id}', response_model=StatusList)
def status_de_compra(
    c_id: int,
    session: Session = Depends(get_session),
):
    query = (
        select(Status).where(Status.c_id == c_id).order_by(Status.created_at)
    )

    return StatusList(statuses=session.scalars(query).all())
