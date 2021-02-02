from corrotina import corrotina


@corrotina
def print_(formatação):
    while True:
        values = yield
        print(formatação.format(*values))


@corrotina
def média(target):
    total = 0.0
    contador = 0
    while True:
        contador += 1
        total += yield
        target.send(
            (contador, total, total/contador)
        )


formatação = print_(
    'Contador: {} - Total: {} - Resultado: {}'
)

# formatação = print_(
#     'A: {} - B: {} - C: {}'
# )

coro = média(target=formatação)
coro.send(10)  # Contador: 1 - Total: 10.0 - Resultado: 10.0
coro.send(20)  # Contador: 2 - Total: 30.0 - Resultado: 15.0
