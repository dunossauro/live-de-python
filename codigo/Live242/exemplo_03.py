from trio import run, open_memory_channel, open_nursery, sleep
from random import randint


async def publisher(sender, range_):
    with sender:
        for x in range_:
            if randint(0, 1):
                await sender.send(f'Mensage: {x}')
            else:
                await sleep(2)
                await sender.send(f'Mensage: {x}')


async def subscriber(nome, recever):
    with recever:
        async for message in recever:
            print(f'|{nome}| Recebido: {message}')


async def main():
    senderA, receverA = open_memory_channel(5)
    senderB, receverB = open_memory_channel(5)

    async with open_nursery() as nursery:
        nursery.start_soon(publisher, senderA, range(5, 15))
        nursery.start_soon(publisher, senderB, range(-10, 4))
        nursery.start_soon(subscriber, 'A', receverA)
        nursery.start_soon(subscriber, 'B', receverB)

run(main)
