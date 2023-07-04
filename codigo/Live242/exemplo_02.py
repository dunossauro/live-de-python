from trio import run, open_nursery, open_file
from httpx import AsyncClient, ConnectTimeout


async def fetch(url):
    async with AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        print(data['id'], data['name'])

    async with await open_file('pokes.csv', 'a') as f:
        await f.write(f'{data["id"]},{data["name"]}\n')


async def main():
    base_url = 'https://pokeapi.co/api/v2/pokemon/{}'
    async with await open_file('pokes.csv', 'w') as f:
        await f.write(f'id,nome')

    try:
        async with open_nursery() as nursery:
            for n in range(1, 100):
                nursery.start_soon(
                    fetch,
                    base_url.format(n)
                )

            print(nursery.child_tasks)

            nursery.start_soon(
                fetch,
                base_url.format(99)
            )
    except *ConnectTimeout as ex:
        print(ex)

        for e in ex.exceptions:
            print(e.request.url)

run(main)
