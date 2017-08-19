"""
Uma breve introdução para entender as rotas.

Objetivo: Dinâmicas e estáticas
"""

from bottle import route, run


@route('/')
def index():
    """Rota estática para o index do site."""
    return '<h1>Olá live de python</h1>'


@route('/<person>')
def hello(person):
    """Exemplo de rota dinâmica."""
    return 'Olá {}'.format(person)


run(port=8080)
