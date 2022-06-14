from psutil import virtual_memory, swap_memory


def bytes_to_gigas(value):
    return f'{value / 1024 / 1024 / 1024: .2f}GB'

print(bytes_to_gigas(virtual_memory().total))

print(bytes_to_gigas(swap_memory().total))

print(bytes_to_gigas(virtual_memory().used))

pesado = list(range(100_000_000))

print(bytes_to_gigas(virtual_memory().used))

del pesado

print(bytes_to_gigas(virtual_memory().used))
