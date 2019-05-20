import click

@click.group('pipes')
def pipes():
    """Utilitarios de pipes"""
    ...

@pipes.command()
@click.option(
    '-f', 'file', default=click.get_text_stream('stdin')
)
@click.option('-w', 'word', type=click.STRING)
@click.option('-n', 'number', is_flag=True)
@click.option('-v', 'verbose', is_flag=True)
def grep(file, word, number, verbose):
    for ind, linha in enumerate(file, 1):
        if word in linha:
            click.secho(
                linha if not number else f'{ind} {linha}',
                fg='red'
            )
        elif verbose:
            click.echo(linha)
