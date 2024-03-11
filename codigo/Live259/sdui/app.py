# exemplo_00.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


pydantic_react = 'https://cdn.jsdelivr.net/npm/@pydantic/fastui-prebuilt@0.0.22/dist/assets/index.js'
css = 'https://unpkg.com/terminal.css@0.7.4/dist/terminal.min.css'

template = """
<html>
    <head>
        <title>{title}</title>
        <meta
            name="fastui:APIRootUrl"
            content="{api_root_url}" />
        <script
            type="module" crossorigin
            src="{pydantic_react}"></script>
        <link
            rel="stylesheet"
            href="{css}" />
    </head>
    <body>
        <div id="root">
        </div>
    </body>
</html>
"""


@app.get('/view/')
async def page():
    return [
        {'type': 'Heading', 'level': 1, 'text': 'Olá mundo!'},
        {'type': 'Paragraph', 'text': 'Nosso primeiro exemplo!'},
        {'type': 'Button', 'text': 'Click 1!'},
        {'type': 'Button', 'text': 'Click 2!'},
        {'type': 'Button', 'text': 'Click 3!'},
        {'type': 'Heading', 'level': 3, 'text': 'Qualquer coisa'},
    ]


@app.get('/{path:path}')
async def html_landing() -> HTMLResponse:
    return HTMLResponse(
        template.format(
            title='Página dahora!',
            pydantic_react=pydantic_react,
            css=css,
            api_root_url='/view',
        )
    )
