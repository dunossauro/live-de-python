from asyncio import get_event_loop, coroutine


@coroutine
def subgenerator():
    return 42


@coroutine
def coro():
    val1 = yield from subgenerator()
    val2 = yield from subgenerator()
    return val1 + val2


loop = get_event_loop()

result = loop.run_until_complete(coro())
print(result)
