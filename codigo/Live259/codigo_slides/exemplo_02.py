from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import FastUI
from fastui import components as c
from fastui import prebuilt_html

app = FastAPI()


@app.get('/api/', response_model=FastUI, response_model_exclude_none=True)
def api():
    return [
        c.Page(
            components=[
                c.Navbar(title='Página de Exemplo'),
                c.Heading(text='Pagina Bacana!', level=1),
                c.Paragraph(text='Boas vindas a nossa incrível página!'),
            ]
        )
    ]


@app.get('/{path:path}')
def home():
    return HTMLResponse(prebuilt_html())
