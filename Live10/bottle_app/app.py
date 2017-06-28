"""Aplicação de testes para o Bottle."""
from bottle import jinja2_view, get, run, post, request, static_file
from base_forms import Cadastro, Login
from re import compile as r_compile


@get('/<path>')
@jinja2_view('generic.html')
def default_pages(path):
    return dict(title=path,
                path=path,
                css_file='/static/style.css',
                lista=['cadastro', 'login'])


@get('/')
@jinja2_view('main.html')
def index():
    return dict(title='Live10',
                css_file='/static/style.css',
                lista=['cadastro', 'login'])


@get('/cadastro')
@jinja2_view('cadastro.html')
def cadastro():
    return dict(title='Cadastro',
                form=Cadastro(),
                css_file='/static/style.css',
                lista=['cadastro', 'login'])


@post('/cadastro')
@jinja2_view('generic.html')
def castro_post():
    name = request.forms.get('name')
    username = request.forms.get('username')
    lastName = request.forms.get('lastName')
    gender = request.forms.get('gender')
    password = request.forms.get('passwd')
    email = request.forms.get('email')
    fullDate = request.forms.get('age')

    regex = r_compile(r'\d{2}/\d{2}/\d{4}')

    if len(password) < 6:
        msg = 'Senha inválida, use ao menos 6 caracteres'
    elif '@' not in email:
        msg = 'Email inválido'
    elif not regex.findall(fullDate):
        msg = 'Data inválida'
    else:
        msg = '''
              Bem vind{} {}
              <br />
              Usuário: {}
              <br />
              Senha: {}'''.format('a' if gender.startswith('f') else 'o',
                                  name,
                                  username,
                                  password)

    return dict(title='Cadastro',
                path=msg,
                css_file='/static/style.css',
                lista=['cadastro', 'login'])


@get('/login')
@jinja2_view('login.html')
def login():
    return dict(title='Login',
                form=Login(),
                css_file='/static/style.css',
                lista=['cadastro', 'login'])


@post('/login')
@jinja2_view('generic.html')
def post_login():
    return dict(title='Cadastro',
                path='Olá {}'.format(request.forms.get('username')),
                css_file='/static/style.css',
                lista=['Novidades', 'Amigos', 'Pessoas', 'Sair'])


@get('/static/<path>')
def static_files(path):
    return static_file('/static/{}'.format(path), root='.')


run(port=8080, ip='192.168.0.106')
