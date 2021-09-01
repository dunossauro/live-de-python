from asyncio import get_event_loop, sleep
from collections.abc import Awaitable
from random import randint


class AsyncRandom(Awaitable):
    def __await__(self):
        return self.randint(1, 100).__await__()

    async def randint(self, start, stop):
        value = randint(start, stop)
        return await sleep(0.2, result=value)


async def main():
    random = AsyncRandom()
    while True:
        print(await random)

loop = get_event_loop()
loop.run_until_complete(main())
