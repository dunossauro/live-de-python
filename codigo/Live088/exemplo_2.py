import click


@click.command()
@click.argument(
    'batatinha', envvar='BATATINHA', type=click.INT
)
def xpto(batatinha):
    click.echo(batatinha)


xpto()
