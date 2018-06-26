from random import shuffle
from itertools import zip_longest
from pprint import pprint


premios = ['Livro de expressões regulres',
           'Livro de OO',
           'Curso: Machine Learning na Prática',
           'Curso: Python para Android, iOS, Windows, Linux, Mac,',
           'Curso: Python Web Scraping',
           'Curso: Python para Todos']

participantes = ['Carlos Damázio',
                 'Gilberto Ferreira',
                 'Rodrigo Prado de Jesus',
                 'Washington da Costa Ferreira',
                 'João Ricardo Lhullier Lugão',
                 'Eliézer Bourchardt',
                 'Kyle Felipe Vieira Roberto',
                 'Lucas Gabriel de Oliveira Bento',
                 'Gabrielly de Andrade da Silva',
                 'Vinícius Loiola Cavalheiro']

shuffle(participantes)

pprint(list(zip_longest(premios, participantes)))

"""
[('Livro de expressões regulres', 'Eliézer Bourchardt'),
 ('Livro de OO', 'João Ricardo Lhullier Lugão'),
 ('Curso: Machine Learning na Prática', 'Kyle Felipe Vieira Roberto'),
 ('Curso: Python para Android, iOS, Windows, Linux, Mac,',
  'Rodrigo Prado de Jesus'),
 ('Curso: Python Web Scraping', 'Lucas Gabriel de Oliveira Bento'),
 ('Curso: Python para Todos', 'Vinícius Loiola Cavalheiro'),
 (None, 'Carlos Damázio'),
 (None, 'Gilberto Ferreira'),
 (None, 'Gabrielly de Andrade da Silva'),
 (None, 'Washington da Costa Ferreira')]
"""
