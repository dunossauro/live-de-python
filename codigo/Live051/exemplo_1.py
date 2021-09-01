"""
Primeira etapa do problema.

Fazer download das imagens dos 100 primeiros pokemons da pokeapi
"""
from datetime import datetime
from os import makedirs
from os.path import exists
from pprint import pprint
from shutil import copyfileobj, rmtree
from urllib.parse import urljoin
from requests import get
path = 'downloads'
base_url = 'https://pokeapi.co/api/v2/'  # NOQA


if exists(path):
    rmtree(path)
makedirs(path)


def download_file(name, url, *, path='downloads', type='png'):
    """Executa o download de um arquivo."""
    xpto = get(url, stream=True)
    with open(f'{path}/{name}.{type}', 'wb') as f:
        copyfileobj(xpto.raw, f)
    return f'{path}/{name}'


def get_sprite_url(url, sprite='front_default'):
    return get(url).json()['sprites'][sprite]


start_time = datetime.now()

# Faz o request inicial da lista dos 100 primeiros pokemons
pokemons = get(urljoin(base_url, 'pokemon/?limit=10')).json()['results']

# Agora temos que entrar na url de cada pokemon para pegar a url da imagem
images_url = {j['name']: get_sprite_url(j['url']) for j in pokemons}

# Agora o download de cada uma das imagens
files = [download_file(name, url) for name, url in images_url.items()]

time_elapsed = datetime.now() - start_time

print('Tempo total (hh:mm:ss.ms) {}'.format(time_elapsed))
pprint(files)
