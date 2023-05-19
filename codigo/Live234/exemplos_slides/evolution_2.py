from httpx import Client
from rich import print

# pokes = ['bulbasaur', 'charmander', 'squirtle', 'caterpie', 'weedle', 'pikachu']
from pokes import pokes

def evolution(poke):
    print(poke)
    with Client(base_url='https://pokeapi.co/api/v2') as client:
        try:
            # request 1
            response = client.get(f'/pokemon/{poke}')
            id_ = response.json().get('id')

            # request 2
            response = client.get(f'/pokemon-species/{id_}')
            evolution = response.json().get('evolution_chain').get('url')

            # request 3
            response = client.get(evolution)
            print(
                response
                .json()
                .get('chain')
                .get('evolves_to')[0]
                .get('species')
                .get('name')
            )
        except Exception as e:
            print(e)

for poke in pokes:
    evolution(poke)
