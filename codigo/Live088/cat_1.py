import click


@click.command()
@click.argument('file')
def cat(file):
    with open(file) as f:
        click.echo(f.read())


cat()
