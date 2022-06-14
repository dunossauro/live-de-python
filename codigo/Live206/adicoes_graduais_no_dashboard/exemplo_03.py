# Incluindo % da CPU
from time import sleep
from dashing import VGauge, VSplit, HSplit, HGauge
from psutil import virtual_memory, swap_memory, cpu_percent

ui = HSplit(  # ui
    HSplit(  # ui.items[0]
        VGauge(title='RAM'),  # ui.items[0].items[0]
        VGauge(title='Swap'),  # ui.items[0].items[0]
        title='Memória',
        border_color=3
    ),
    VSplit(  # ui.items[1]
        HGauge('CPU %'),  # ui.items[1].items[1]
        title='CPU',
        border_color=5
    ),
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

    # # CPU
    cpu_tui = ui.items[1]
    # CPU %
    cpu_percent_tui = cpu_tui.items[0]
    ps_cpu_percent = cpu_percent()
    cpu_percent_tui.value = ps_cpu_percent
    cpu_percent_tui.title = f'CPU {ps_cpu_percent}%'

    try:
        ui.display()
        sleep(.5)
    except KeyboardInterrupt:
        break
