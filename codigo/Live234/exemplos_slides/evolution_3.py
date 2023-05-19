from asyncio import all_tasks, gather, run
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
    result = gather(*[evolution(poke) for poke in pokes])
    print("Tarefas pendentes antes de 'await':", all_tasks())
    await result
    print("Tarefas pendentes após de 'await':", all_tasks())


run(main())
