# FastUI

## TOC

- [Contexto](#contexto)
- [FastUI](#fastui): O básico
- [Referências](#referências)

FastaUI é um projeto criado pela galera do Pydantic e ainda em progresso.

Atualmente na versão 0.5.2
Licença MIT


## Contexto

Os milhares de conceitos por trás dessa aplicação!

### APIs REST

## FastUI
O básico

### Instalação

```bash
pip install fastui
```

### Olá mundo!

```python
# exemplo_00.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import AnyComponent, FastUI, prebuilt_html
from fastui import components as c

app = FastAPI()


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def page() -> list[AnyComponent]:
    return [
        c.Page(
            components=[
                c.Heading(text='Olá mundo!'),
                c.Paragraph(text='Nosso primeiro exemplo!'),
            ],
        ),
    ]


@app.get("/{path:path}")
async def html_landing() -> HTMLResponse:
    return HTMLResponse(prebuilt_html(title='Olá Mundo'))
```

#### Os milhoes de conceitos por trás disso!

O endpoint `/{path:path}` é o endpoint mais abrangente que se pode criar com o fastapi. Ele literalmente vai cobrir qualquer requisição que seja feita a aplicação e que não tenha um endpoint registrado anteriormente.


Nisso, ele responde um HTML, esse HTML é gerado pelo `prebuilt_html`. Que faz uma requisição **por padrão** para `/api/` que retorna um objeto JSON, com o esquema definido pelo modelo do Pydantic `FastUI`.


Se fizermos uma requisição para `/api/`, podemos ver o retorno:

```python
[
  {
    "components": [
      {
        "text": "Olá mundo!",
        "level": 1,
        "type": "Heading"
      },
      {
        "text": "Nosso primeiro exemplo!",
        "type": "Paragraph"
      },
      {
        "text": "Click!",
        "namedStyle": "primary",
        "type": "Button"
      }
    ],
    "type": "Page"
  }
]
```

Que contém o schema que retornamos no próprio endpoint:

```python
    return [
        c.Page(
            components=[
                c.Heading(text='Olá mundo!'),
                c.Paragraph(text='Nosso primeiro exemplo!'),
            ],
        ),
    ]
```

Esse schema é recebido pela aplicação no front e a página é contrída dinâmicamente.


## Referências

### Vídeos
Talk Python - Building UIs in Python with FastUI : https://youtu.be/DzyxUVm_1cI

### Código
Repositório: https://github.com/pydantic/FastUI

### Livro
Hypermedia systems: https://hypermedia.systems/

### Documentações
REST - Explained For Beginners: https://htmx.org/essays/rest-explained/
