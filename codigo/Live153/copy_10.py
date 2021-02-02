def acumular():
    contador = 0
    while True:
        valor = yield

        if valor is None:
            return contador

        contador += valor


def agregador_de_contadores(contadores):
    while True:
        contador = yield from acumular()
        contadores.append(contador)


contadores = []

agregador = agregador_de_contadores(contadores)  # Inicia o gerador delegante
next(agregador)  # Preparação

for i in range(4):
    agregador.send(i)

agregador.send(None)  # 6
