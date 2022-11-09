from rich import box
from rich.console import Console
from rich.panel import Panel

c = Console()

t = '''

Live de [red]Python[/red]! :heart_decoration:

sobre [reverse][b]RICH[/b][/] :fire:

Hoje às 22h :clock10:

Venha aprender a fazer [blink][reverse][blue]prints[/blue][/reverse][/blink] incríveis!
'''
c.rule('Convite :warning:')
c.print(
    Panel.fit(
        t,
        box=box.DOUBLE_EDGE,
    ),
    justify='center'
)
c.rule(':warning:')
