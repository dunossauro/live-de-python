from collections import namedtuple

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


coro = média()
next(coro)  # preparação

coro.send(10)  # 10.0
coro.send(20)  # 15.0

try:
    coro.send(None)
except StopIteration as ex:
    print(ex.value)
