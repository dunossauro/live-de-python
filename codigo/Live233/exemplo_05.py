from typer import Context, Exit, Typer, Option
from rich import print

app = Typer()

__version__ = '0.0.1a0'


def version(arg):
    if arg:
        print(__version__)
        raise Exit(code=0)


@app.callback(invoke_without_command=True)
def callcaback(
    ctx: Context,
    version: bool = Option(
        False,
        '--version', '-v', '--versao',
        callback=version,
        is_eager=True,
        is_flag=True,
        case_sensitive=False
    )
):
    if ctx.invoked_subcommand:
        return
    print(
        'Use os seguintes comandos [b]batata[/] ou [b]comando-a[/]'
    )

@app.command()
def comando_a():
    print('Comando A')


@app.command(name='batata', help='Comando Batata!')
def comando_b(nome: str):
    print('Comando B')


app()
