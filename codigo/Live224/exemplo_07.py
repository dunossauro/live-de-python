from rich import print, box
from rich.panel import Panel
from rich.text import Text

t = Text(':snake: JLX :snake:', justify='center')
t.stylize('white on blue b')

print(Panel(
    t,
    style='red',
    box=box.DOUBLE_EDGE,
    title='DAVID',
    subtitle='batatinhas fritas'
))
