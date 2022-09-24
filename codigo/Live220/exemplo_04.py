from asyncio import TaskGroup, run, sleep


async def coro(arg):
    print(f'Inicirou a CORO: {arg=}')
    await sleep(1)
    print(f'Terminou a CORO: {arg=}')

async def coro2():
    print(f'Inicirou 2')
    await sleep(10)
    print(f'Terminou 2')
    return 1


async def main():
    async with TaskGroup() as tg:
        task = tg.create_task(coro2())
        tg.create_task(coro(2))
        tg.create_task(coro(3))
        task_result = await task
        tg.create_task(coro(task_result))
        tg.create_task(coro(4))
        tg.create_task(coro(5))


run(main())
