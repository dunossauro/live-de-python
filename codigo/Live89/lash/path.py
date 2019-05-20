from os.path import abspath
from shutil import copy, copytree
import click

@click.group('paths')
def paths():
    """Utilitarios de paths"""
    ...

@paths.command()
@click.argument('de', type=click.Path(exists=True))
@click.argument('para', type=click.Path())
@click.option(
    '-r', 'recursive',
    is_flag=True, default=False
)
def cp(de, para, recursive):
    """Copia arquivos DE um lugar PARA outro."""
    if recursive:
        copytree(abspath(de), abspath(para))
    else:
        copy(abspath(de), abspath(para))


@paths.command()
@click.option('-f', 'file', type=click.File(mode='r'))
def less(file):
    """Lê um arquivo usando paginação."""
    click.echo_via_pager(
        f'{linha}\n' for linha in file.readlines()
    )
