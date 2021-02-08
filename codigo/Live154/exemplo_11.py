from collections import namedtuple
from pprint import pprint


Result = namedtuple('Result', 'total media contador')


def média():
    total = 0.0
    contador = 0
    média = None
    while True:
        entrada = yield média
        if entrada is None:
            break
        total += entrada
        contador += 1
        média = total/contador
    return Result(total, média, contador)


def agrupador(resultados, chave):
    while True:
        resultados[chave] = yield from média()


def cliente(data):
    results = {}
    for key, values in data.items():
        group = agrupador(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)

    # pprint(results)

    report(results)


def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} média {:.2f} {}'.format(
              result.contador, group, result.media, unit))


data = {
    'garotas;peso':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'garotas;altura':
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'garotos;peso':
        [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'garotos;altura':
        [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}


cliente(data)
