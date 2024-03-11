from typing import Annotated

from fastapi import FastAPI, Form
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory='templates')

database = [
    {'id': 1, 'nome': 'batatinha', 'telefone': '92892828'},
    {'id': 2, 'nome': 'Serjão berranteiro', 'telefone': '0999909099'},
    {'id': 3, 'nome': 'Sonic the Hedgehog', 'telefone': '1231231456'},
    {'id': 4, 'nome': 'Tails', 'telefone': '92821736'},
]


@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        name='index.html', request=request, context={'data': database}
    )


@app.get('/cadastro', response_class=HTMLResponse)
def get_cadastro(request: Request):
    return templates.TemplateResponse(
        name='cadastro.html',
        request=request,
    )


@app.post('/cadastro', response_class=HTMLResponse)
def post_cadastro(
    nome: Annotated[str, Form()], telefone: Annotated[str, Form()]
):
    database.append(dict(id=len(database) + 1, nome=nome, telefone=telefone))
    return RedirectResponse(url='/', status_code=303)
