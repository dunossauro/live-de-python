"""
Cookies.

Objetivo: entender o responde, como setar os cookies
"""
from bottle import request, route, run, response


@route('/')
def hello_again():
    if request.get_cookie("visited"):
        return "Olá, bem vindo de volta"
    else:
        response.set_cookie("visited", "yes")
        return "Olá, é um prazer conhecer você"


run(port=8080)
