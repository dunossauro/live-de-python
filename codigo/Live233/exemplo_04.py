from typer import Argument, Exit, Option, run
from rich import print

__version__ = '0.0.1a0'


def version(arg):
    if arg:
        print(__version__)
        raise Exit(code=0)


def lower(val):
    return val.lower()


def olar(
    nome: str = Argument(
        ..., help='Seu primeiro nome', callback=lower
    ),
    email: str = Argument(..., metavar='<email>@dudu.com'),
    senha: str = Option(
        ...,
        prompt=True,
        hide_input=True,
        confirmation_prompt=True,
        help='A senha será perguntada no prompt!'
    ),
    version: bool = Option(
        False,
        '--version', '-v', '--versao',
        callback=version,
        is_eager=True,
        is_flag=True,
        case_sensitive=False
    )
):
    print(f'{nome=}, {email=}, {senha=}')


run(olar)
