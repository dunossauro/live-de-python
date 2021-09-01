import click


@click.command()
@click.argument('file', type=click.File('r'))
@click.argument('lines', type=click.BOOL)
def cat(file, lines):
    click.echo(file.read())


cat()
