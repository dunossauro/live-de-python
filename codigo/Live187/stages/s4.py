from httpx import get,post
m=print
e='dunossauro'
F='meu_segrdo_123'
class MinhaClasse:
 def __init__(N):
  N.atributo=7
 def a(N):
  return N.atributo
def M():
 n=get('http://google.com')
 return n
def I(user,passw):
 n=post('http://meusite.com',json={'password':passw,'username':user})
 return n
m(M())
m(I(e,F))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

