from collections import namedtuple
from pprint import pprint
from bs4 import BeautifulSoup as bs
from requests import get


def get_last_page(url: str) -> str:
    pyjobs = get(url)
    pyjobs_page = bs(pyjobs.text, 'html.parser')
    links = pyjobs_page.find('ul', {'class': 'pagination'}).find_all('a')
    return max([link.get('href') for link in links])


def trata_strs(string: str) -> str:
    """Remove rótulos de descrição das caixas."""
    return string.split(':')[1].strip()


def gen_jobs(url: str) -> namedtuple:
    """
    Retorna um iterável com as vagas da página passada.

    Args:
        - url: link da página quais as vagas vão ser retiradas
    """
    pyjobs = get(url)
    pyjobs_page = bs(pyjobs.text, 'html.parser')
    boxes = pyjobs_page.find_all('div', {'class': 'col-md-10'})

    for box in boxes:
        titulo = box.find('h3').text
        ps = box.find_all('p')
        empresa = ps[0].text
        tipo = ps[1].text
        local = ps[3].text

        yield vaga(titulo, trata_strs(empresa),
                   trata_strs(tipo), trata_strs(local))


vaga = namedtuple('Vaga', 'Titulo empresa tipo local')
base_url = 'http://pyjobs.com.br/'
jobs = f'{base_url}jobs/'
job_pages = f'{jobs}?page='

last_page = int(get_last_page(jobs)[-1])
urls = ['{}{}'.format(job_pages, n) for n in range(1, last_page+1)]

for url in urls:
    pprint(list(gen_jobs(url)))
