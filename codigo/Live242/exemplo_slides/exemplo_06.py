from trio import open_memory_channel, open_nursery, run


async def producer(send_channel):
    async with send_channel:
        for i in range(10):
            await send_channel.send(f'message {i}')


async def consumer(receive_channel):
    async with receive_channel:
        async for value in receive_channel:
            print(f'got value {value}')


async def main():
    async with open_nursery() as nursery:
        send_channel, receive_channel = open_memory_channel(0)
        nursery.start_soon(producer, send_channel)
        nursery.start_soon(consumer, receive_channel)

run(main)
