from httpx import get,post
r=print
m='dunossauro'
A='meu_segrdo_123'
class MinhaClasse:
 def __init__(t):
  t.atributo=7
 def metodo(t):
  return t.atributo
def is_google_on():
 h=get('http://google.com')
 return h
def login(user,passw):
 h=post('http://meusite.com',json={'password':passw,'username':user})
 return h
r(is_google_on())
r(login(m,A))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

