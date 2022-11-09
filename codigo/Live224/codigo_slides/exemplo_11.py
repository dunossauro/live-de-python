from rich import print
from rich.text import Text
from rich.panel import Panel

text = Text('Batatinha')
text.justify = 'center'
text.stylize('red b u reverse')

print(Panel(text))

from rich.table import Table
table = Table()
table.add_column(text)
table.add_row(text)
print(table)
