"""
Primeira etapa do problema.

Fazer download das imagens dos 100 primeiros pokemons da pokeapi.

Sincrono: 2m e 16s

- Threads
- multprocess
- concurrence.feautes
- asyncio
"""
from contextlib import contextmanager
from datetime import datetime
from os import makedirs
from os.path import exists
from pprint import pprint
from shutil import rmtree, copyfileobj
from urllib.parse import urljoin
from requests import get

path = 'dowload'
base_url = 'http://pokeapi.co/api/v2/'

if exists(path):
    rmtree(path)
makedirs(path)


@contextmanager
def timeit(*args):
    start_time = datetime.now()
    yield
    time_elapsed = datetime.now() - start_time
    print(f'Tempo total (hh:mm:ss.ms) {time_elapsed}')


def download_file(name, url, *, path=path, type_='png'):
    """Faz o download de um arquivo."""
    response = get(url, stream=True)
    fname = f'{path}/{name}.{type_}'
    with open(fname, 'wb') as f:
        copyfileobj(response.raw, f)
    return fname


def get_sprite_url(url, sprite='front_default'):
    return get(url).json()['sprites'][sprite]


with timeit() as t:
    pokemons = get(urljoin(base_url, 'pokemon/?limit=100')).json()['results']
    images_url = {j['name']: get_sprite_url(j['url']) for j in pokemons}
    files = [download_file(name, url) for name, url in images_url.items()]


pprint(files)
