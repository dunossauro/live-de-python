from asyncio import get_event_loop, coroutine

@coroutine
def print_async(msg: str) -> None:
    print(f'ASYNC: {msg}')

async def print_async(msg: str) -> None:
    print(f'ASYNC: {msg}')


loop = get_event_loop()
loop.run_until_complete(print_async('oi'))
loop.close()
