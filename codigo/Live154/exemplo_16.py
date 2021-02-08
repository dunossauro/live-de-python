from asyncio import (
    get_event_loop, gather, sleep
)


async def subgenerator():
    await sleep(1)
    return 42


async def coro():
    val1 = await subgenerator()
    val2 = await subgenerator()
    return val1 + val2


loop = get_event_loop()
grupo = gather(*[coro() for i in range(20)])
result = loop.run_until_complete(grupo)
print(result)
