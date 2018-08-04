from asyncio import get_event_loop
from collections.abc import Awaitable

class AsyncYield(Awaitable):
    def __init__(self, value):
        self.value = value
        self._loop = get_event_loop()

    def do(self):
        return self.value

    def __await__(self):
        result = yield from self._loop.run_in_executor(None, self.do)
        return result


async def main():
    result = await AsyncYield(10)
    return result


l = get_event_loop()
print(l.run_until_complete(main()))
