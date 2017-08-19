"""
Exemplo usando um formulário WEB.

Objetivo: entender 'request'
"""
from bottle import route, run, request


@route('/', method='GET')
def index_get():
    """Exemplo do metodo get expondo os forms."""
    return '''
     <form action="/" method="post">
        Username: <input name="username" type="text" />
        Password: <input name="password" type="password" />
        <input value="Login" type="submit" />
    </form>
    '''


@route('/', method='POST')
def index_post():
    """Exemplo do metodo POST recebendo os dados do form."""
    username = request.forms.get('username')
    password = request.forms.get('password')

    return """
     <h1>Suas informações</h1>
     </br>
     <h4>{}</h4>
     <h4>{}</h4>
     """.format(username, password)


run(port=8080)
