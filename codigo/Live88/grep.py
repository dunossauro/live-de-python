import click


@click.command()
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


grep()
