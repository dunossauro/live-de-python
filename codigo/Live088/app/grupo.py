from os import listdir
import click


@click.group('cli')
def cli():
    ...


@cli.command('ls', help='Lista arquivos em um path')
@click.argument('path')
@click.option(
    '-l', '--list', is_flag=True,
    help='Define se serão apresentados em lista'
)
def ls(path, list):
    path = listdir(path)
    if not list:
        click.echo(path)
    else:
        for e in path:
            click.echo(e)


@cli.command('cat', help='Printa um arquivo na tela')
@click.argument('file')
def cat(file):
    with open(file) as f:
        click.echo(f.read())


@cli.command('grep', help='Emula o grep')
@click.argument('file', type=click.File('r'))
@click.option(
    '-w', '--word', 'word',
    default='', type=click.STRING,
    help='palavra que vai dar match'
)
def grep(file, word):
    for linha in file.readlines():
        if word in linha:
            click.echo(
                click.style(linha, fg='green', bg='black')
            )
        else:
            click.echo(linha)

cli()
