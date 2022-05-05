from asyncio import run, gather, sleep
from aiopath import AsyncPath


async def espera():
    print("Comecei a espera")
    await sleep(20)
    print("Terminei a espera")


async def lista_arquivos():
    print('Comecei a listar arquivos')
    path = AsyncPath(".")
    r = [file async for file in path.glob("*")]
    print('terminei de listar arquivos')
    return r


async def executa():
    result = await gather(
        espera(),
        lista_arquivos(),
        espera(),
        lista_arquivos(),
        lista_arquivos(),
        lista_arquivos(),
        espera(),
    )
    return result


run(executa())
