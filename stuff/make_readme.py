from csv import DictReader
from dataclasses import dataclass, field
from pathlib import Path
from re import sub
from typing import TypedDict, cast
from urllib.error import HTTPError
from urllib.request import urlopen

base_url = 'https://github.com/dunossauro/live-de-python/blob/main'

@dataclass
class Live:
    numero: str
    titulo: str
    link: str
    codigo: str = field(init=False)
    slide: str = field(init=False)

    def markdownify(self):
        if self.slide and self.codigo:
            print(
                f'|{self.numero}|[link]({self.link})|[codigo]({self.codigo})|[slide]({self.slide})|{self.titulo}|'
            )
        elif not self.slide and not self.codigo:
            print(
                f'|{self.numero}|[link]({self.link})|||{self.titulo}|'
            )
        elif not self.slide:
            print(
                f'|{self.numero}|[link]({self.link})|[codigo]({self.codigo})||{self.titulo}|'
            )
        elif not self.codigo:
            print(
                f'|{self.numero}|[link]({self.link})||[slide]({self.slide})|{self.titulo}|'
            )

    def fetch(self, url):
        try:
            with urlopen(url):
                return url
        except HTTPError as e:
            return ''

    def __post_init__(self):
        slide_url = f'{base_url}/slides/Live%20de%20Python%20%23{self.numero.zfill(3)}.pdf'
        self.slide = self.fetch(slide_url)

        codigo_url = f'{base_url}/codigo/Live{self.numero.zfill(3)}'

        self.codigo = self.fetch(codigo_url)


class Row(TypedDict):
    tema: str
    data: str
    link: str
    tags: str


csv = Path('lives.csv').open()

for line in DictReader(csv, delimiter=';'):
    line = cast(Row, line)

    if (
        '#' in line['tema']
        and 'Live' in line['tema']
        and 'special' not in line['tema']
    ):
        fatiado = line['tema'].replace(' | ', ' - ').strip().partition(' - ')
        parte_a, _, parte_b = fatiado
        if parte_a.strip().startswith('Live'):
            parte_a, parte_b = parte_b, parte_a

        teste = sub(r'([Ll]ive( de [Pp]ython)? \s?#)', '', parte_b)
        if len(teste) > 3:
            split = teste.split(' - ')
            parte_a = parte_a + ' - ' + split[-1]
            parte_b = split[0]

        if parte_b.startswith('Live'):
            parte_b = sub(r'(.*#)(\d+)', r'\2', parte_b)

        live = Live(
            numero=parte_b.strip(),
            titulo=parte_a.strip(),
            link=line['link'],
        )

        live.markdownify()
