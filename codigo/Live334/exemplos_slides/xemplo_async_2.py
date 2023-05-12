import asyncio
from rich import print


async def minha_corotina(nome):
    print("Início da corotina: ", nome)
    await asyncio.sleep(1)
    print("Meio da corotina: ", nome)
    await asyncio.sleep(1)
    print("Fim da corotina: ", nome)


async def main():
    tasks = asyncio.gather(
        *[minha_corotina(n) for n in range(3)]
    )
    print("Tarefas pendentes antes de 'await':", asyncio.all_tasks())

    await tasks
    print("Tarefas pendentes após 'await':", asyncio.all_tasks())


asyncio.run(main())
