from rich import print
from rich.layout import Layout
from rich.panel import Panel
from rich.console import Group
from rich.text import Text
from rich.markdown import Markdown
from rich.table import Table

t = Table(title='Tabela do meio')

t.add_column('XPTO', style='bold green')
t.add_row('Sei não')

texto = '''
# Meu texto

Isso sim que é legal de fazer.

1. Lado direito
2. no centro outra coisa
3. na direita, vish. Um painel!
'''

l = Layout()

l2 = Layout()

l2.split_column(
    Group(
        Panel('CIMA'),
        Text('Tô em cima IHUUUUU!', justify='center')
    ),
    t,
)

l.split_row(
    Panel('Esquerda'),
    l2,
    Markdown(texto)
)

print(l)
