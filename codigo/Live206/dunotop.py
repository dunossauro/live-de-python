from datetime import datetime
from time import sleep
from dashing import HSplit, VSplit, VGauge, HGauge, Text
from psutil import (
    virtual_memory,
    swap_memory,
    cpu_percent,
    sensors_temperatures,
    sensors_battery,
    disk_io_counters,
    disk_partitions,
    disk_usage,
    net_io_counters,
    net_if_addrs,
    users,
    boot_time,
    pids,
    process_iter
)


def bytes_to_gigas(value):
    return value / 1024 / 1024 / 1024


ui = HSplit(  # ui
    VSplit(
        Text(
            ' ',
            border_color=9,
            title='Processos'
        ),
        HSplit(  # ui.items[0]
            VGauge(title='RAM'),  # ui.items[0].items[0]
            VGauge(title='SWAP'),  # ui.items[0].items[1]
            title='Memória',
            border_color=3
        ),
    ),
    VSplit(  # ui.items[1]
        HGauge(title='CPU %'),
        HGauge(title='cpu_0'),
        HGauge(title='cpu_1'),
        HGauge(title='cpu_2'),
        HGauge(title='cpu_3'),
        HGauge(title='cpu_4'),
        HGauge(title='cpu_5'),
        HGauge(title='cpu_6'),
        HGauge(title='cpu_7'),
        HGauge(title='CPU Temp'),
        HGauge(title='PCH Temp'),
        title='CPU',
        border_color=5,
    ),
    VSplit(  # ui.items[2]
        Text(
            ' ',
            title='Outros',
            border_color=4
        ),
        Text(
            ' ',
            title='Disco',
            border_color=6
        ),
        Text(
            ' ',
            title='Rede',
            border_color=7
        ),
    ),
)


while True:
    # # Processos
    proc_tui = ui.items[0].items[0]
    p_list = []
    for proc in process_iter():
        proc_info = proc.as_dict(['name', 'cpu_percent'])
        if proc_info['cpu_percent'] > 0:
            p_list.append(proc_info)

    ordenados = sorted(
        p_list,
        key=lambda p: p['cpu_percent'],
        reverse=True
    )[:10]
    proc_tui.text = f"{'Nome':<30}CPU"

    for proc in ordenados:
        proc_tui.text += f"\n{proc['name']:<30} {proc['cpu_percent']}"

    
    
    # # Memória
    mem_tui = ui.items[0].items[1]
    # Ram
    ram_tui = mem_tui.items[0]
    ram_tui.value = virtual_memory().percent
    ram_tui.title = f'RAM {ram_tui.value} %'

    # SWAP
    swap_tui = mem_tui.items[1]
    swap_tui.value = swap_memory().percent
    swap_tui.title = f'SWAP {swap_tui.value} %'

    # # CPU
    cpu_tui = ui.items[1]
    # CPU %
    cpu_percent_tui = cpu_tui.items[0]
    ps_cpu_percent = cpu_percent()
    cpu_percent_tui.value = ps_cpu_percent
    cpu_percent_tui.title = f'CPU {ps_cpu_percent}%'

    # Porcentagem dos cores
    cores_tui = cpu_tui.items[1:9]
    ps_cpu_percent = cpu_percent(percpu=True)
    for i, (core, value) in enumerate(zip(cores_tui, ps_cpu_percent)):
        core.value = value
        core.title = f'cpu_{i} {value}%'

    # CPU TEMP
    cpu_temp_tui = cpu_tui.items[9]
    ps_cpu_temp = sensors_temperatures()['coretemp'][0]
    cpu_temp_tui.value = ps_cpu_temp.current
    cpu_temp_tui.title = f'CPU Temp {ps_cpu_temp.current}C'

    # PCH TEMP
    pch_temp_tui = cpu_tui.items[10]
    ps_pch_temp = sensors_temperatures()['pch_skylake'][0]
    pch_temp_tui.value = ps_pch_temp.current
    pch_temp_tui.title = f'CPU Temp {ps_pch_temp.current}C'

    # # Outros
    outros_tui = ui.items[2].items[0]
    outros_tui.text = f'Bateria: {sensors_battery().percent}%'
    outros_tui.text += f'\nUsuário: {users()[0].name}'
    boot = datetime.fromtimestamp(boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    outros_tui.text += f'\nHorário do boot: {boot}'
    outros_tui.text += f'\nProcessos: {len(pids())}'

    # # Disco
    disk_tui = ui.items[2].items[1]
    partitions = disk_partitions()
    counters = disk_io_counters(perdisk=True)

    disk_tui.text = f"{'Partição':<10}{'Uso':<6}{'Lido':<6}{'Escrito'}"

    for partition in partitions:
        partition_name_counter = partition.device.split('/')[-1]
        disk_bytes = counters[partition_name_counter]

        disk_tui.text += '\n{:<10}{:<6}{:<6.2f}{:.2f}'.format(
            partition.mountpoint,
            disk_usage(partition.mountpoint).percent,
            bytes_to_gigas(disk_bytes.read_bytes),
            bytes_to_gigas(disk_bytes.write_bytes)
        )

    # # Rede
    network_tui = ui.items[2].items[2]
    addrs_v4 = net_if_addrs()['wlp2s0'][0]
    addrs_v6 = net_if_addrs()['wlp2s0'][1]
    network_tui.text = f'IPV4: {addrs_v4.address}\n'
    network_tui.text += f'MaskV4: {addrs_v4.netmask}\n'
    network_tui.text += f'IPV6: {addrs_v6.address[:10]}\n'
    network_tui.text += f'MaskV6: {addrs_v6.netmask}\n'

    network_tui.text += f'Enviado: {bytes_to_gigas(net_io_counters().bytes_sent):.2f}GB\n'
    network_tui.text += f'Recebido: {bytes_to_gigas(net_io_counters().bytes_recv):.2f}GB\n'
    
    
    try:
        ui.display()
        sleep(1)
    except KeyboardInterrupt:
        break
