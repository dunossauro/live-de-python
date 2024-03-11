from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

templates = Jinja2Templates(directory='templates')
app.mount('/assets', StaticFiles(directory='assets'), name='assets')

database = [
    {'id': 1, 'nome': 'batatinha', 'telefone': '92892828'},
    {'id': 2, 'nome': 'Serjão berranteiro', 'telefone': '0999909099'},
    {'id': 3, 'nome': 'Sonic the Hedgehog', 'telefone': '1231231456'},
    {'id': 4, 'nome': 'Tails', 'telefone': '92821736'},
]


class DataIn(BaseModel):
    nome: str
    telefone: str


class DataOut(BaseModel):
    id: int
    nome: str
    telefone: str


@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        name='index.html', request=request, context={'data': database}
    )


@app.get('/data', response_model=list[DataOut])
def data():
    return database


@app.post('/cadastro')
def post_cadastro(data: DataIn):
    database.append(dict(id=len(database) + 1, **data.model_dump()))
