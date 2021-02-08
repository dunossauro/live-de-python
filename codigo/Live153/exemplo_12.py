from asyncio import coroutine, get_event_loop


@coroutine
def coro():
    print('42')


print(type(coro))
print(type(coro()))

loop = get_event_loop()
loop.run_until_complete(coro())
