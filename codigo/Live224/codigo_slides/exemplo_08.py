from rich.console import Console
from rich.tree import Tree

c = Console()
t = Tree(label=':red_circle: - Arvore')

g1 = t.add('Galho 1')
g2 = t.add('Galho 2')
g3 = t.add('Galho 3')

g1.add('1')
g1.add('2')
g1.add('3')

g2.add('4')

g3.add('5')
g3.add('6')

c.print(t)
