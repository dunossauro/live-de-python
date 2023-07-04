from trio import move_on_after, open_file, open_nursery, run
from httpx import AsyncClient


async def fetch_and_write(url):
    async with AsyncClient() as client:

        with move_on_after(3):

            response = await client.get(url)
            data = response.json()
            async with await open_file('pokes.csv', 'a') as f:
                await f.write(f"{data['id']},{data['name']}\n")


async def main():
    url = 'https://pokeapi.co/api/v2/pokemon/{}'
    try:
        async with open_nursery() as nursery:
            for n in range(1, 11):
                poke_url = url.format(n)
                print(f'Iniciando: {poke_url}')
                nursery.start_soon(fetch_and_write, poke_url)

run(main)
