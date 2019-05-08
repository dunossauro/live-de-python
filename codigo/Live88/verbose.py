import click


@click.command()
@click.option('-v', '--verbose', count=True)
def verbose(verbose):
    click.echo(verbose)


verbose()
