from time import sleep
from threading import Event, Thread
from queue import Queue
from urllib.parse import urljoin
from requests import get
from functions import target, timeit

base_url = 'http://pokeapi.co/api/v2/'
event = Event()
fila = Queue(maxsize=101)


def get_urls():
    pokemons = get(urljoin(base_url, 'pokemon/?limit=100')).json()['results']
    [fila.put(pokemon) for pokemon in pokemons]
    event.set()
    fila.put('Kill')


class Worker(Thread):
    def __init__(self, target, queue, *, name='Worker'):
        super().__init__()
        self.name = name
        self.queue = queue
        self._target = target
        self._stoped = False
        print(self.name, 'started')

    def run(self):
        event.wait()
        while not self.queue.empty():
            pokemon = self.queue.get()
            print(self.name, pokemon)
            if pokemon == 'Kill':
                self.queue.put(pokemon)
                self._stoped = True
                break
            self._target(pokemon)

    def join(self):
        while not self._stoped:
            sleep(0.1)


def get_pool(n_th: int):
    """Retorna um número n de Threads."""
    return [Worker(target=target, queue=fila, name=f'Worker{n}')
            for n in range(n_th)]


with timeit():
    get_urls()
    print(fila.queue)
    thrs = get_pool(10)
    print('starts')
    [th.start() for th in thrs]
    print('joins')
    [th.join() for th in thrs]
