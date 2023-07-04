# # -- Trio
# import trio


# async def main():
#     print('Olá Trio!')


# trio.run(main)

# # -- Asyncio 01
# import asyncio


# async def main():
#     print('Olá Trio!')


# asyncio.run(main())

# -- Asyncio 02
import asyncio


async def main():
    print('Olá Future!')


loop = asyncio.get_event_loop()
future = asyncio.ensure_future(main())
future.add_done_callback(
    lambda future: print(f'Future: {future.get_name()} completo')
)

try:
    loop.run_until_complete(future)
finally:
    loop.close()


# -- Asyncio 03
import asyncio


async def main():
    print('Olá Task!')


loop = asyncio.get_event_loop()
task = asyncio.create_task(main())
task.add_done_callback(
    lambda task: print(f'Future: {task.get_name()} completo')
)

loop.run_forever()
