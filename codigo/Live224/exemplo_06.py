from rich import print
from rich.console import Group
from rich.table import Table

t = Table(title='XPTO')
t.add_column('xpto')
t2 = Table(title='Batatas')
t2.add_column('xpto')

g = Group(  # renderizavel
    '[red on white b] É nois[/]',
    'TEXTO',
    'Linha do fim',
    t, t2
)

print(g)
