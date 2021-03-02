from asyncio import get_event_loop, gather
from httpx import AsyncClient

base_url = 'https://pokeapi.co/api/v2/pokemon/{number}'


async def subgenerator(number):
    print(f'Antes {number}')
    async with AsyncClient() as client:
        response = await client.get(
            base_url.format(number=number),
            timeout=None
        )
        print(f'Depois {number}')
        # print(number, response.json()['name'])
        return number, response.json()['name']


async def coro():
    return await gather(
        *[subgenerator(number) for number in range(1, 10)],
    )


loop = get_event_loop()
result = loop.run_until_complete(coro())
result = loop.run_until_complete(subgenerator(55))

from pprint import pprint
pprint(result)
