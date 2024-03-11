from typing import Annotated

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastui import AnyComponent, FastUI
from fastui import components as c
from fastui import prebuilt_html
from fastui.components.display import DisplayLookup
from fastui.events import BackEvent, GoToEvent
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    nome: str
    telefone: str


database: list[User] = [User(id=1, nome='Sonic', telefone='12123')]


@app.get('/api/', response_model=FastUI, response_model_exclude_none=True)
def api() -> list[AnyComponent]:
    return [
        c.Page(
            components=[
                c.Navbar(
                    title='App!',
                    start_links=[
                        c.Link(
                            components=[c.Text(text='Listar')],
                            on_click=GoToEvent(url='/'),
                        ),
                        c.Link(
                            components=[c.Text(text='Criar!')],
                            on_click=GoToEvent(url='/cadastro'),
                        ),
                    ],
                ),
                c.Heading(text='Pessoas na Base', level=1),
                c.Table(
                    data=database,
                    columns=[
                        DisplayLookup(
                            field='id',
                            on_click=GoToEvent(url='/user_show/{id}'),
                        ),
                        DisplayLookup(field='nome'),
                        DisplayLookup(field='telefone'),
                    ],
                ),
            ]
        )
    ]


@app.get(
    '/api/user_edit/{user_id}',
    response_model=FastUI,
    response_model_exclude_none=True,
)
def edit_user(user_id: int):
    user = database[user_id - 1]
    return [
        c.Page(
            components=[
                c.Form(
                    submit_url='/editar',
                    form_fields=[
                        c.FormFieldInput(
                            name='id',
                            title='id:',
                            initial=user.id,
                            locked=True,
                        ),
                        c.FormFieldInput(
                            name='nome', title='Nome:', initial=user.nome
                        ),
                        c.FormFieldInput(
                            name='telefone',
                            title='Telefone:',
                            initial=user.telefone,
                        ),
                    ],
                )
            ]
        )
    ]


@app.get(
    '/api/user_show/{user_id}',
    response_model=FastUI,
    response_model_exclude_none=True,
)
def get_user(user_id: int):
    user = database[user_id - 1]
    return [
        c.Page(
            components=[
                c.Heading(text=user.nome),
                c.Details(data=user),
                c.Div(
                    components=[
                        c.Button(text='Voltar', on_click=BackEvent()),
                        c.Button(
                            text='Editar',
                            named_style='secondary',
                            on_click=GoToEvent(url=f'/user_edit/{user.id}'),
                        ),
                        c.Button(
                            text='Deletar!',
                            named_style='warning',
                            on_click=GoToEvent(url=f'/deletar/{user.id}'),
                        ),
                    ],
                ),
            ]
        )
    ]


@app.get(
    '/api/cadastro', response_model=FastUI, response_model_exclude_none=True
)
def api() -> list[AnyComponent]:
    return [
        c.Page(
            components=[
                c.Navbar(title='App!'),
                c.Heading(text='Meu Texto!', level=1),
                c.Form(
                    submit_url='/cadastro',
                    form_fields=[
                        c.FormFieldInput(title='Nome:', name='nome'),
                        c.FormFieldInput(title='Telefone:', name='telefone'),
                    ],
                ),
            ]
        )
    ]


@app.post('/cadastro', response_model=FastUI, response_model_exclude_none=True)
def cadastro(nome: Annotated[str, Form()], telefone: Annotated[str, Form()]):
    database.append(User(id=len(database) + 1, nome=nome, telefone=telefone))
    return [c.FireEvent(event=GoToEvent(url='/'))]


@app.post('/editar', response_model=FastUI, response_model_exclude_none=True)
def editar(
    id: Annotated[int, Form()],
    nome: Annotated[str, Form()],
    telefone: Annotated[str, Form()],
):
    database[id - 1] = User(id=id, nome=nome, telefone=telefone)
    return [c.FireEvent(event=GoToEvent(url='/'))]


@app.get(
    '/api/deletar/{id}',
    response_model=FastUI,
    response_model_exclude_none=True,
)
def deletar(id: int):
    print('Entrei no delete!')
    del database[id - 1]
    return [c.FireEvent(event=GoToEvent(url='/'))]


@app.get('/{path:path}')
def home():
    return HTMLResponse(prebuilt_html(title='Nossa página legal!'))
