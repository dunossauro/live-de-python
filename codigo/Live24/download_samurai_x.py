from collections import namedtuple
from requests import get
from bs4 import BeautifulSoup as bs

ep_structure = namedtuple('EP', 'temporada episodio nome')
URL = 'https://pt.wikipedia.org/wiki/Lista_de_epis%C3%B3dios_de_Samurai_X'

request = get(URL)

page = bs(request.content, 'lxml')
tables = page.findAll('table', {'class': 'wikitable'})

# Divisão de tabelas por temporada
temp_1, temp_2, temp_3 = tables


def get_rows(table):
    return table.findAll('tr')[1:]


# Linhas por tabela de temporada
t1_rows, t2_rows, t3_rows = map(get_rows, [temp_1, temp_2, temp_3])


# t1_rows[0].find_all('td')[0].text
# t1_rows[0].find_all('td')[3].text


def get_data(temp: int, rows: list) -> namedtuple:
    for row in rows:
        columns = row.find_all('td')
        ep = columns[0].text
        nome = columns[3].text
        yield ep_structure(temp, int(ep), nome)


# Dados por linha de cada temporada
t1_data, t2_data, t3_data = map(lambda t: list(get_data(t[0], t[1])),
                                enumerate([t1_rows, t2_rows, t3_rows], 1))

# Lista de todos os episodios
lista_episodios = sum([t1_data, t2_data, t3_data], [])
