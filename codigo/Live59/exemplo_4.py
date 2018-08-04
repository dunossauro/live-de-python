from asyncio import get_event_loop
from types import coroutine


class AsyncContextManager:
    async def __aenter__(self):
        print('Entrando no contexto')

    async def __aexit__(self, *args):
        print('Saindo do contexto')


async def run():
    print('estou fora do batatinhas')
    async with AsyncContextManager() as batatinhas:
        print(batatinhas)
        print('Estou em batatinhas')
    print('estou fora do batatinhas')


l = get_event_loop()
l.run_until_complete(run())
