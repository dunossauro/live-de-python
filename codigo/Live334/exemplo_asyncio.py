from asyncio import all_tasks, create_task, run, sleep
from rich import print


async def olar(val, delay=1):
    print(f'Início da corrotina {val}')
    await sleep(delay)
    print(f'Meio da corrotina {val}')
    await sleep(delay)
    print(f'Fim da corrotina {val}')


async def main():
    task1 = create_task(olar(1, .1))  # Corrotina
    task2 = create_task(olar(2))  # Corrotina
    task3 = create_task(olar(3))  # Corrotina
    task4 = create_task(olar(4))  # Corrotina
    print('Fila de Taks: ', all_tasks())

    await task1
    await task2
    await task3
    await task4
    print('Fila de Taks: ', all_tasks())


run(main())  # Corrotina
