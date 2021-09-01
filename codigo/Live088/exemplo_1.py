import click


@click.command()
@click.argument('nome')
def live(nome):
    click.echo(f'Oi {nome}')


live()
