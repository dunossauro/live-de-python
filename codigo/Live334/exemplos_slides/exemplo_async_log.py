import asyncio
import logging


async def minha_corotina():
    print("Início da corotina")
    await asyncio.sleep(1)
    print("Fim da corotina")


async def main():
    tarefa1 = asyncio.create_task(minha_corotina())
    tarefa2 = asyncio.create_task(minha_corotina())

    await tarefa1
    await tarefa2

# Configuração do logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('asyncio')
logger.setLevel(logging.DEBUG)

# Ativa o modo de depuração do asyncio
asyncio.run(main(), debug=True)
