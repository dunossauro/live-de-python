import asyncio


async def corrotina(i):
    print(f'Iniciando corrotina {i}')
    await asyncio.sleep(i)
    print(f'Terminando corrotina {i}')


async def main():
    asyncio.create_task(corrotina(1))
    asyncio.create_task(corrotina(2))
    asyncio.create_task(corrotina(3))

    for x in range(5):
        print(f'Ihuu {x}')


asyncio.run(main())
