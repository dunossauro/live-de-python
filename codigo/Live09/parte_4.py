"""
Templates.

Basicamente o entendimento de como renderizar templates
"""
from bottle import jinja2_view, route, run, request, response


@route('/<area>')
@jinja2_view('paginas/teste.html')
def teste(area):
    """Rederizando uma view com o decorador do jinja."""
    return dict(nome=area)


@route('/')
@jinja2_view('paginas/index.html')
def index():
    """Rederizando uma view com o decorador do jinja."""
    links = ['home', 'about', 'help']

    return dict(links=links)


@route('/user', method='GET')
@jinja2_view('paginas/user.html')
def user():
    """Uma página básica de login que usa cookies."""
    links = ['home', 'about', 'help']

    return dict(links=links)


@route('/user', method='POST')
@jinja2_view('paginas/user.html')
def user_post():
    """Uma página básica de login que usa cookies."""
    username = request.forms.get('username')
    password = request.forms.get('password')

    if username == 'eduardo' and password == 'senha' or \
       request.get_cookie("user") == 'eduardo':

        response.set_cookie("user", "eduardo")
        links = ['home', 'user_space', 'metrics', 'help']
        return dict(string='Você está logado', links=links)
    else:
        response.set_cookie("user", "None")
        return """
        <h1> ERRO ao efetuar loggin</h1>
        """


run(port=8080)
