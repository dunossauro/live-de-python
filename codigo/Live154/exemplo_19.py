from asyncio import gather, get_event_loop, sleep
from httpx import AsyncClient


base_url = 'https://pokeapi.co/api/v2/pokemon/{number}'


async def um(loop):
    """tampolim."""
    await sleep(1)
    print(1)
    loop.call_later(1, um, loop)


async def download(number):
    async with AsyncClient() as client:
        response = await client.get(
            base_url.format(number=number),
            timeout=None
        )
        print(number)
        return number, response.json()['name']


loop = get_event_loop()

# loop.call_soon(
#     gather,
#     *[download(number) for number in range(5, 10)]
# )

# loop.call_later(
#     10,
#     gather,
#     *[download(number) for number in range(1, 5)]
# )
# loop.call_later(
#     10,
#     gather,
#     *[download(number) for number in range(90, 100)]
# )

# loop.call_later(
#     15,
#     gather,
#     *[download(number) for number in range(100, 105)]
# )

loop.run_until_complete(um(loop))

# loop.run_forever()
