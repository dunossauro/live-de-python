from httpx import get,post
s=print
username='dunossauro'
password='meu_segrdo_123'
class MinhaClasse:
 def __init__(self):
  self.atributo=7
 def metodo(self):
  return self.atributo
def is_google_on():
 response=get('http://google.com')
 return response
def login(user,passw):
 response=post('http://meusite.com',json={'password':passw,'username':user})
 return response
s(is_google_on())
s(login(username,password))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

