from rich import print, box
from rich.table import Table


t = Table(
    title='Tabela de gastos sem sentido :warning:',
    box=box.SIMPLE
)

t.add_column('Onde gastei')
t.add_column('Quanto gastei', justify='center')
t.add_column(
    'Precisava?',
    style='green',
    justify='right',
    no_wrap=True
)

t.add_row('Rolê', '200,00', 'Não!')
t.add_row('Farmácia', '40,00', 'SIM')

print(t)
