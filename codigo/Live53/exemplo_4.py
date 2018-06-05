"""Exemplo de Pool nativo."""
from multiprocessing import Pool
# from multiprocessing.dummy import Pool
from os import getpid
from pprint import pprint

# workers = Pool(5)


def soma_2(x):
    return x + 2, getpid()


workers = Pool(5)

# sync
result = workers.map(soma_2, range(100))
pprint(result)

# async
result = workers.map_async(soma_2, range(100))
pprint('bananas')
result.wait()
pprint('bananas2')
pprint(result.get())
