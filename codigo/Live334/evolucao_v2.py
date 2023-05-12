from httpx import Client

# pokemons = ['bulbasaur', 'charmander', 'squirtle']

from pokes import pokes as pokemons


def evolucao(poke):
    print(f'Entrada: {poke}')
    with Client(base_url='https://pokeapi.co/api/v2') as client:
        # request 1
        response = client.get(f'/pokemon/{poke}')
        id_ = response.json().get('id')

        # request 2
        response = client.get(f'/pokemon-species/{id_}')
        evolution_chain = (
            response
            .json()
            .get('evolution_chain')
            .get('url')
        )

        # request 3
        response = client.get(evolution_chain)
        evolution_name = (
            response
            .json()
            .get('chain')
            .get('evolves_to')[0]
            .get('species')
            .get('name')
        )
        print(f'Saída de {poke} -> {evolution_name}')

for poke in pokemons:
    evolucao(poke)
