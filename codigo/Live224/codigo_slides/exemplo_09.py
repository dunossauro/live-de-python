from rich.console import Console, Group
from rich.table import Table

console = Console()
table = Table()

table.add_column('nome', style='green')
table.add_column('idade', style='blue', justify='center')
table.add_column('emoji', justify='right')
table.add_row('Eduardo', '[blink]29[/]', ':heart:')

g = Group(
    '[red on yellow b] Batatinhas[/]',
    '[r blink] fritas[/]',
    table,
)

console.print(g)
