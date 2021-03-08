from datetime import datetime
import fire
from httpx import get
from parsel import Selector


def hora():
    return datetime.now()


def dolar():
    response = get('https://economia.awesomeapi.com.br/json/all/USD').json()
    return response['USD']['high']


def tv(canal):
    response = get(f'https://meuguia.tv/programacao/canal/{canal}').text
    s = Selector(response)
    return {
        'nome': s.css('h2::text').get(),
        'inicio': s.css('div.time::text').get(),
        'tipo': s.css('h3::text').get(),
    }


class Jogos:
    def megasena(self):
        response = get(
            'https://lotericas.io/api/v1/jogos/megasena/lasted'
        ).json()
        return response['data'][0]['dezenasSorteadasOrdemSorteio']

    def quina(self):
        response = get(
            'https://lotericas.io/api/v1/jogos/quina/lasted'
        ).json()
        return response['data'][0]['dezenasSorteadasOrdemSorteio']


fire.Fire()
