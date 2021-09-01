from bs4 import BeautifulSoup as bs
from requests import get

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('banda', type=str,
                    help='nome da banda')

args = parser.parse_args()                    

from functions import pretty_format, get_lirycs, dict_to_json

base_url = 'https://www.letras.mus.br/'
band = 'dead-fish/'
html = get('{}{}'.format(base_url, band)).text

page = bs(html, 'lxml')
xpto = page.find('ul', {'class': 'cnt-list'})
lines = xpto.find_all('li')

musics_links = {line.text: line.find('a').get('href') for line in lines}


all_ = {music: pretty_format(get_lirycs(base_url, musics_links, music))
        for music in musics_links}

dict_to_json('dead-fish', all_)
