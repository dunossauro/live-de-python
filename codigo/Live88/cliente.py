import click


@click.command()
@click.option('-n', '--name', prompt=True)
@click.option('-a', '--age', prompt=True, type=click.INT)
def cliente(name, age):
    click.echo(name, age)


cliente()
