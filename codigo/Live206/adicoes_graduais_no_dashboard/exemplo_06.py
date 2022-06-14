# Adicionando Bateria
from time import sleep
from dashing import VGauge, VSplit, HSplit, HGauge, Text
from psutil import (
    sensors_battery,
    virtual_memory,
    swap_memory,
    cpu_percent,
    sensors_temperatures
)

ui = HSplit(  # ui
    HSplit(  # ui.items[0]
        VGauge(title='RAM'),  # ui.items[0].items[0]
        VGauge(title='Swap'),  # ui.items[0].items[0]
        title='Memória',
        border_color=3
    ),
    VSplit(  # ui.items[1]
        HGauge(title='CPU %'),  # ui.items[1].items[0]
        HGauge(title='cpu_0'),  # ui.items[1].items[1]
        HGauge(title='cpu_1'),  # ui.items[1].items[2]
        HGauge(title='cpu_2'),  # ui.items[1].items[3]
        HGauge(title='cpu_3'),  # ui.items[1].items[4]
        HGauge(title='cpu_4'),  # ui.items[1].items[5]
        HGauge(title='cpu_5'),  # ui.items[1].items[6]
        HGauge(title='cpu_6'),  # ui.items[1].items[7]
        HGauge(title='cpu_7'),  # ui.items[1].items[8]
        HGauge(title='CPU Temp'),  # ui.items[1].items[9]
        HGauge(title='PCH Temp'),  # ui.items[1].items[10]
        title='CPU',
        border_color=5
    ),
    VSplit(  # ui.items[2]
        Text(  # ui.items[2].items[0]
            ' ',
            title='Outros',
            border_color=4),
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

    # Porcentagem dos cores
    cores = cpu_tui.items[1:9]
    for i, (core, value) in enumerate(zip(cores, cpu_percent(percpu=True))):
        core.value = value
        core.title = f'cpu_{i} {value}%'

    # Temperatura CPU
    cpu_temp_tui = cpu_tui.items[9]
    ps_cpu_temp = sensors_temperatures()['coretemp'][0].current
    cpu_temp_tui.value = ps_cpu_temp
    cpu_temp_tui.title = f'CPU Temp {ps_cpu_temp}C'

    # Temperatura PCH
    pch_temp_tui = cpu_tui.items[10]
    ps_pch_temp = sensors_temperatures()['pch_skylake'][0].current
    pch_temp_tui.value = ps_pch_temp
    pch_temp_tui.title = f'PCH Temp {ps_pch_temp}C'

    # # Outros
    outros_tui = ui.items[2].items[0]
    # Bateria
    outros_tui.text = f'Bateria: {sensors_battery().percent}%'
    
    

    try:
        ui.display()
        sleep(.5)
    except KeyboardInterrupt:
        break
