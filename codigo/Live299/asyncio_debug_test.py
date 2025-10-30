from asyncio import gather, run, sleep as asleep
from time import sleep

async def maybe():
    print('maybe')
    await asleep(10)


async def task(n):
    print(f'task start - {n}')
    if n % 2:
        await maybe()
    await asleep(10)
    print(f'task end - {n}')


async def main():
    while True:
        sleep(3)
        await gather(*[task(x) for x in range(10)])

run(main())

