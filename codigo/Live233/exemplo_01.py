from typer import run
from rich import print


def olar(nome: str):
    print(f'Olar [b][red]{nome}[/]')


run(olar)
