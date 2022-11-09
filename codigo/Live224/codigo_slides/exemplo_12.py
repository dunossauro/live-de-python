from rich import print
from rich.layout import Layout
from rich.panel import Panel

l = Layout()
centro = Layout()

centro.split_column(
    Panel('Cima'),
    Panel('baixo'),
)

l.split_row(
    Panel('Esquerdo'),
    Panel('Centro'),
    Panel('Direito'),
)


print(l)
