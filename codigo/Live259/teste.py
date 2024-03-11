from typing import Annotated
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastui import FastUI, prebuilt_html, components as c
from fastui import AnyComponent
from fastui import events
from fastui.components.display import DisplayLookup
from pydantic import BaseModel


app = FastAPI()
form_string: Annotated[str, Form()]

class User(BaseModel):
    id: int
    nome: str
    telefone: str


database: list[User] = [
    User(id=1, nome='Sergião berranteiro', telefone='123123')
]

navbar = c.Navbar(title='APP!', start_links=[
    c.Link(
        on_click=events.GoToEvent(url='/cadastro'),
        components=[
            c.Text(text='Cadastro!'),
        ]
    ),
    c.Link(
        on_click=events.GoToEvent(url='/listar'),
        components=[
            c.Text(text='Listar!'),
        ]
    )
])


@app.get(
    '/api/',
    response_model=FastUI,
    response_model_exclude_none=True
)
def api() -> list[AnyComponent]:
    return [
        c.FireEvent(event=events.GoToEvent(url='/listar'))
    ]


@app.get(
    '/api/cadastro',
    response_model=FastUI,
    response_model_exclude_none=True,
)
def cadastro() -> list[AnyComponent]:
    return [
        c.Page(components=[
            navbar,
            c.Form(
                submit_url='/cadastro',
                form_fields=[
                    c.forms.FormFieldInput(
                        name='nome', title='Nome:'
                    ),
                    c.forms.FormFieldInput(
                        name='telefone', title='Telefone:'
                    )
                ])
        ])
    ]

@app.get(
    '/api/listar',
    response_model=FastUI,
    response_model_exclude_none=True,
)
def listar() -> list[AnyComponent]:
    return [
        c.Page(components=[
            navbar,
            c.Heading(text='Listagem!'),
            c.Table(
                data=database,
                data_model=User,
                columns=[
                    DisplayLookup(
                        field='id',
                        on_click=events.GoToEvent(
                            url='/detalhes/{id}'
                        )
                    ),
                    DisplayLookup(field='nome'),
                    DisplayLookup(field='telefone'),
                ]
            ),
            c.Button(
                text='Criar!',
                on_click=events.GoToEvent(url='/cadastro')
            )
        ])
    ]


@app.get(
    '/api/detalhes/{user_id}',
    response_model=FastUI,
    response_model_exclude_none=True,
)
def editar(user_id: int) -> list[AnyComponent]:
    user = database[user_id - 1]
    return [
        c.Page(components=[
            navbar,
            c.Heading(text='Detalhes!'),
            c.Heading(text=user.nome, level=3),
            c.Details(data=user),
            c.Button(
                text='Editar',
                named_style='primary',
                on_click=events.GoToEvent(url=f'/editar/{user_id}')
            ),
            c.Button(
                text='Voltar!',
                on_click=events.BackEvent(),
                named_style='secondary',
            ),
            c.Button(
                text='Deletar!',
                named_style='warning',
                on_click=events.GoToEvent(
                    url=f'/deletar/{user_id}'
                )
            ),
        ]),
    ]


@app.get(
    '/api/deletar/{user_id}',
    response_model=FastUI,
    response_model_exclude_none=True,
)
def deletar(user_id: int) -> list[AnyComponent]:
    del database[user_id - 1]
    return [c.FireEvent(event=events.GoToEvent(url='/listar'))]


@app.get(
    '/api/editar/{user_id}',
    response_model=FastUI,
    response_model_exclude_none=True,
)
def editar(user_id: int) -> list[AnyComponent]:
    user = database[user_id - 1]
    return [
        c.Page(components=[
            navbar,
            c.Heading(text='Editar!'),
            c.Form(
                submit_url='/editar',
                form_fields=[
                    c.FormFieldInput(
                        name='id',
                        title='ID:',
                        initial=user.id,
                        locked=True
                    ),
                    c.FormFieldInput(
                        name='nome',
                        title='Nome: ',
                        initial=user.nome
                    ),
                    c.FormFieldInput(
                        name='telefone',
                        title='Telefone: ',
                        initial=user.telefone
                    ),
                ]
            )
        ])
    ]

@app.post('/cadastro')
def cadastro(
    nome: str = Form(), telefone: str = Form()
) -> list[AnyComponent]:
    database.append(
        User(id=len(database) + 1, nome=nome, telefone=telefone)
    )
    return [
        c.FireEvent(event=events.GoToEvent(url='/listar'))
    ]


@app.post('/editar')
def editar(
    id: int = Form(), nome: str = Form(), telefone: str = Form()
):
    database[id - 1] = User(
        id=id, nome=nome, telefone=telefone
    )
    return [
        c.FireEvent(event=events.GoToEvent(url='/listar'))
    ]


@app.get('/{path:path}')
def home():
    return HTMLResponse(prebuilt_html(title='CRUD da massa!'))
