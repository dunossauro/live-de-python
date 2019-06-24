d = {'chave': 'valor'}

d # {'chave': 'valor'}
e = {'chave': 'valor2'}

d.update(e)
d # {'chave': 'valor2'}

f = {7: 'sete'}
f # {7: 'sete'}

d.update(f)
d # {'chave': 'valor2', 7: 'sete'}

d.keys() # dict_keys(['chave', 7])

d.values() # dict_values(['valor2', 'sete'])

d.items() # dict_items([('chave', 'valor2'), (7, 'sete')])
