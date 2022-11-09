from rich.panel import Panel
from rich.console import Console, Group
from rich import box

c = Console()

g = Group(
    Panel('Live', border_style='red on white'),
    Panel('de', box=box.ASCII2),
    Panel('[red]Python![/]')
)

c.print(g)
