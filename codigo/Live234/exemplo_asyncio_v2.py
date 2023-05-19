from asyncio import all_tasks, create_task, gather, run, sleep
from rich import print


async def olar(val, delay=1):
    print(f'Início da corrotina {val}')
    await sleep(delay)
    print(f'Meio da corrotina {val}')
    await sleep(delay)
    print(f'Fim da corrotina {val}')

    return val


async def main():
    tasks = gather(
        olar(100, 5), *[olar(n) for n in range(30)]
    )
    print('Fila de Taks: ', all_tasks())

    result = await tasks
    print('Fila de Taks: ', all_tasks())
    print(result)

run(main())  # Corrotina
