from httpx import get,post
r=print
u='dunossauro'
d='meu_segrdo_123'
class MinhaClasse:
 def __init__(l):
  l.atributo=7
 def metodo(l):
  return l.atributo
def is_google_on():
 w=get('http://google.com')
 return w
def login(user,passw):
 w=post('http://meusite.com',json={'password':passw,'username':user})
 return w
r(is_google_on())
r(login(u,d))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

