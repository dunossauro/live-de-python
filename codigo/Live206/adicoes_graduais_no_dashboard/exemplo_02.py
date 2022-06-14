# Incluindo Swap
from time import sleep
from dashing import VGauge, HSplit
from psutil import virtual_memory, swap_memory

ui = HSplit(  # ui
    HSplit(  # ui.items[0]
        VGauge(title='RAM'),  # ui.items[0].items[0]
        VGauge(title='Swap'),  # ui.items[0].items[0]
        title='Memória',
        border_color=3
    )
)


while True:
    # # Memoria
    # RAM
    ram_tui = ui.items[0].items[0]
    memoria = virtual_memory().percent
    ram_tui.title = f'RAM {memoria} %'
    ram_tui.value = memoria
    # SWAP
    swap_tui = ui.items[0].items[1]
    memoria = swap_memory().percent
    swap_tui.title = f'SWAP {memoria} %'
    swap_tui.value = memoria

    try:
        ui.display()
        sleep(.5)
    except KeyboardInterrupt:
        break
