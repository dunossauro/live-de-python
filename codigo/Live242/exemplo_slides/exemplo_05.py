from trio import open_file, open_nursery, run
from httpx import AsyncClient, ConnectTimeout


async def fetch_and_write(url):
    print('  | Entrando em fetch_and_write')
    async with AsyncClient() as client:
        print(f'    | Fazendo request: {url}')
        response = await client.get(url, timeout=.1)
        data = response.json()
    async with await open_file('pokes.csv', 'a') as f:
        print(f'    | escrevendo no arquivo: {url}')
        await f.write(f"{data['id']},{data['name']}\n")


async def main():
    url = 'https://pokeapi.co/api/v2/pokemon/{}'
    try:
        async with open_nursery() as nursery:
            for n in range(1, 11):
                poke_url = url.format(n)
                print(f'Iniciando: {poke_url}')
                nursery.start_soon(fetch_and_write, poke_url)

    # Exceptions de todo o nursery
    except *ConnectTimeout as ex:
        for error in ex.exceptions:
            print(f'ERROR: {error.request.url}')

run(main)
