import asyncio
from rich import print


async def minha_corotina(nome):
    print("Início da corotina: ", nome)
    await asyncio.sleep(1)
    print("Meio da corotina: ", nome)
    await asyncio.sleep(1)
    print("Fim da corotina: ", nome)


async def main():
    tarefa1 = asyncio.create_task(minha_corotina(1))
    tarefa2 = asyncio.create_task(minha_corotina(2))
    tarefa3 = asyncio.create_task(minha_corotina(3))
    print("Tarefas pendentes antes de 'await':", asyncio.all_tasks())

    await tarefa1
    await tarefa2
    await tarefa3
    print("Tarefas pendentes após 'await':", asyncio.all_tasks())


asyncio.run(main())
