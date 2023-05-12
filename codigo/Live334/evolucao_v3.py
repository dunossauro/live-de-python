from asyncio import gather, run
from httpx import AsyncClient
from rich import print
from pokes import pokes

# pokes = ['bulbasaur', 'charmander', 'squirtle']


async def evolucao(poke):
    async with AsyncClient(
        base_url='https://pokeapi.co/api/v2'
    ) as client:
        print(f'request 1: [b][red]{poke}[/]')
        response = await client.get(f'/pokemon/{poke}')
        id_ = response.json().get('id')

        # request 2
        print(f'request 2: [b][green]{poke}[/]')
        response = await client.get(f'/pokemon-species/{id_}')
        evolution_chain = (
            response
            .json()
            .get('evolution_chain')
            .get('url')
        )

        # request 3
        print(f'request 3: [b][blue]{poke}[/]')
        response = await client.get(evolution_chain)
        evolution_name = (
            response
            .json()
            .get('chain')
            .get('evolves_to')[0]
            .get('species')
            .get('name')
        )
    # print(evolution_name)

async def main():
    result = gather(
        *[evolucao(poke) for poke in pokes]
    )

    await result


run(main())
