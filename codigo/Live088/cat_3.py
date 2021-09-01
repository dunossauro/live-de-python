import click


@click.command()
@click.argument('file', type=click.File('r'))
@click.argument('lines', type=click.BOOL)
def cat(file, lines):
    if not lines:
        click.echo(file.read())
    else:
        for n, line in enumerate(file.readlines()):
            click.echo(f'{n} {line}')


cat()
