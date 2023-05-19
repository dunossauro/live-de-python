from asyncio import all_tasks, gather, run
from aiometer import run_all
from httpx import AsyncClient
from rich import print

pokes = ['bulbasaur', 'charmander', 'squirtle', 'caterpie', 'weedle', 'pikachu']
# from pokes import pokes

async def evolution(poke):
    print('Pokemon: ', poke)
    async with AsyncClient(base_url='https://pokeapi.co/api/v2') as client:
        try:
            # request 1
            response = await client.get(f'/pokemon/{poke}')
            id_ = response.json().get('id')

            # request 2
            response = await client.get(f'/pokemon-species/{id_}')
            evolution = response.json().get('evolution_chain').get('url')

            # request 3
            response = await client.get(evolution)
            print(
                'Evolução: ', (
                    response
                    .json()
                    .get('chain')
                    .get('evolves_to')[0]
                    .get('species')
                    .get('name')
                )
            )
        except Exception as e:
            print(f'Erro: {poke} - {e}')



async def main():
    from functools import partial
    from aiometer import run_all
    # result = gather(*[evolution(poke) for poke in pokes])
    result = run_all(
        [partial(evolution, poke) for poke in pokes],
        max_at_once=2,
        max_per_second=2
    )
    await result


run(main())
