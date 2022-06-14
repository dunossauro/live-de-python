from dashing import VGauge, VSplit, HSplit
from psutil import virtual_memory
from time import sleep

ui = HSplit(  # ui
    VSplit(  # ui.items[0]
        VGauge(title='RAM'),  # ui.items[0].items[0]
        title='Memória',
        border_color=3
    )
)


while True:
    # # Memoria
    ram_tui = ui.items[0].items[0]
    memoria = virtual_memory().percent
    ram_tui.title = f'RAM {memoria} %'
    ram_tui.value = memoria
    try:
        ui.display()
        sleep(.5)
    except KeyboardInterrupt:
        break
