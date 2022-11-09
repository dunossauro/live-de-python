from rich import print
from rich.tree import Tree

t = Tree('. :red_circle:')

batata = t.add('Batatinha frita :snake:')

seg = t.add('[red]Segundo ramo da arvore[/]')

seg.add('1')
seg.add('2')
seg.add('3')

batata.add('Frita')
batata.add('Cozida')
batata.add('Assada')

print(t)
