from fastapi import Form
from fastui.components import FireEvent
from fastui.events import GoToEvent, BackEvent

c.Button(text='Clicka em Mim', on_click=GoToEvent(url='/lugar'))
c.Button(text='Clicka em Mim', on_click=BackEvent())

@app.app('/api/lugar')
def resposta_do_form(nome: str = Form()):
    # Faz algo com o form
    return [
        FireEvent(event=GoToEvent(url='/lugar'))
    ]
