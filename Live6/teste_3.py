"""
closure
"""

from pdb import set_trace

# Ola, Ahoy, hello

def externa(id):
    dic = {'pt': 'Olá', 'pi': 'Ahoy', 'en': 'hello'}
    def interna(nome):
        print('{} {}'.format(dic[id], nome))
    return interna

func = externa('pt')
func('Pedro')
func('Julio')
func('Marivaldo')

func = externa('pi')
func('Pedro')
func('Julio')
func('Marivaldo')
