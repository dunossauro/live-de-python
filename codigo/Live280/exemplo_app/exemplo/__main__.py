from cyclopts import App
from rich import print

app = App()


@app.default
def olar(nome: str):
    print(f'Olar {nome}!')


app()
