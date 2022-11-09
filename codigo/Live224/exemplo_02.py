from rich.console import Console
from rich.traceback import install

install(show_locals=True)

c = Console(record=True)

c.print('[yellow on red b] É isso aí[/]!')
c.log('[yellow on red b] ESSE É O LOG[/]!', justify='center')

a = 1
b = 'b'
c = []

# a + b

# b + a

c + a

c.save_html('shell.html')
