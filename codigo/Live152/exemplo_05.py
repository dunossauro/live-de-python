from corrotina import corrotina


@corrotina
def média():
    total = 0.0
    contador = 0
    média = None
    while True:
        entrada = yield média
        total += entrada
        contador += 1
        média = total/contador


coro = média()
coro.next(10)  # 10.0
coro.next(20)  # 15.0
