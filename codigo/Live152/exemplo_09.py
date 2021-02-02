from collections import namedtuple
from corrotina import corrotina

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


@corrotina
def quem_delega():
    result = yield from média()
    yield result


coro = quem_delega()

coro.send(10)  # 10.0
coro.send(20)  # 15.0
coro.send(None)  # Result(total=30.0, media=15.0, contador=2)
