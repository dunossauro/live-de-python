from trio import run, open_nursery
from httpx import AsyncClient


async def fetch(url):
    async with AsyncClient() as client:
        response = await client.get(url, timeout=None)
        data = response.json()
        print(data['id'], data['name'])


async def main():
    base_url = 'https://pokeapi.co/api/v2/pokemon/{}'

    async with open_nursery() as nursery:
        for n in range(1, 11):
            poke_url = base_url.format(n)
            nursery.start_soon(fetch, poke_url)

        print(nursery.child_tasks)


run(main)
