from concurrent.futures import ThreadPoolExecutor

values = range(100_000)


with ThreadPoolExecutor(max_workers=8) as executor:
    resultados = executor.map(
        lambda x: x * x, values
    )


print("Resultados:", list(resultados))
