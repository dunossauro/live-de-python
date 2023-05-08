from typer import run
from rich import print


def olar(
    nome: str,
    email: str,
    senha: str = 'batatinha'
):
    print(f'{nome=}, {email=}, {senha=}')


run(olar)
