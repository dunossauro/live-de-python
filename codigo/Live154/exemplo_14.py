from asyncio import (
    coroutine, get_event_loop, gather
)


@coroutine
def subgenerator():
    return 42


@coroutine
def coro():
    val1 = yield from subgenerator()
    val2 = yield from subgenerator()
    return val1 + val2


loop = get_event_loop()
grupo = gather(coro(), coro(), coro())
result = loop.run_until_complete(grupo)
print(result)
