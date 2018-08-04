from asyncio import get_event_loop, sleep, ensure_future, gather
from collections.abc import AsyncIterator
from types import coroutine
from functools import singledispatch
from typing import Collection, Dict
from io import IOBase


@singledispatch
@coroutine
def aiter(iterator):
    pass

@aiter.register(Collection)
@coroutine
def col_aiter(iterator):
    yield from iterator


@aiter.register(IOBase)
@coroutine
def col_aiter(iterator):
    yield from iterator


@aiter.register(Dict)
@coroutine
def col_aiter(iterator):
    yield from iterator.items()



class AsyncCollection(AsyncIterator):
    def __init__(self, col: Collection, *, loop=None):
        self._iterator = aiter(col)
        self._loop = loop or get_event_loop()

    def __aiter__(self):
        return self

    async def __anext__(self):
        value = await self._loop.run_in_executor(
            None, next, self._iterator, self
        )
        if value is self:
            raise StopAsyncIteration
        return await sleep(0.1, result=value)


lista = 'batatas'
lista2 = [1, 2, 3, 4]
dicionario = {1: 'batatinhas'}


async def run_loop(obj):
    async for val in AsyncCollection(obj):
        print(val)

async def run_loop_file():
    with open('exemplo_1.py') as file:
        async for line in AsyncCollection(file):
            print(line)

async def main():
    future1 = ensure_future(run_loop(lista))
    future2 = ensure_future(run_loop(lista2))
    future3 = ensure_future(run_loop_file())

    result = gather(future3, future1, future2)
    await result

loop = get_event_loop()
loop.run_until_complete(main())
