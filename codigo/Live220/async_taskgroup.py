# Exemplo mais avançado
from asyncio import TaskGroup, sleep, run
from random import randint


async def gen():
    for x in range(10):
        yield x


async def t2():
    # raise KeyError()
    return 'DONE!'


async def task(val):
    print(f'start {val=}')
    r = randint(1, 6)
    await sleep(r)
    if r %2 == 0:
        print(f'ERROR! {val=}')
        raise AssertionError
    print(val)
    return val


async def main():
    async with TaskGroup() as tg:
        done = tg.create_task(t2())
        [tg.create_task(task(val)) async for val in gen()]

        print(await done)

run(main())

# # Exemplo básico
# from asyncio import TaskGroup, run


# async def astr(val):
#     return f'{val=}'


# async def main():
#     async with TaskGroup() as tg:
#         task = tg.create_task(astr('Teste TaskGroup!'))

#         result = await task
#     return result

# result = run(main())

# print(result)
