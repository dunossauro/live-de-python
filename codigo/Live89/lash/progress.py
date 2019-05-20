from time import sleep
from urllib.request import urlopen
import click


@click.command()
@click.option('-l', default=10)
@click.option('-time', default=1)
def pb(l, time):
    with click.progressbar(
        range(l),
        label='??',
        fill_char='>',
        empty_char='.',
        bar_template='a%(label)s [%(bar)s] %(info)s'
) as p:
        for e in p:
            sleep(time)


@click.command()
@click.argument('url', type=click.STRING)
@click.option('-t', 'times', default=1)
def check_url(url, times):
    """Checa se URL está disponível."""
    with click.progressbar(range(times)) as p:
        for e in p:
            if urlopen(url).status != 200:
                click.secho('\tERROR!', fg='green')
