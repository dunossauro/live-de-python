from asyncio import gather, get_event_loop, set_event_loop_policy
from httpx import AsyncClient
import uvloop
set_event_loop_policy(uvloop.EventLoopPolicy())


base_url = 'https://pokeapi.co/api/v2/pokemon/{number}'


async def download(number):
    async with AsyncClient() as client:
        response = await client.get(
            base_url.format(number=number),
            timeout=None
        )
        print(number)
        return number, response.json()['name']


loop = get_event_loop()

loop.call_soon(
    gather,
    *[download(number) for number in range(5, 10)]
)

loop.call_later(
    10,
    gather,
    *[download(number) for number in range(1, 5)]
)
loop.call_later(
    10,
    gather,
    *[download(number) for number in range(90, 100)]
)

loop.run_forever()
