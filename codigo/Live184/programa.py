def altera_linha(linha: str) -> str:
    lista_linha = linha.replace("\n", "").split(" ")
    return " ".join(lista_linha[::-1]) + "\n"


def transcreve_invertido(entrada_path: str, saida_path: str):
    with open(saida_path, "w") as saida:
        with open(entrada_path, "r") as entrada:
            for linha in entrada.readlines():
                saida.write(altera_linha(linha))


if __name__ == "__main__":
    transcreve_invertido("./entrada.txt", "./saida.txt")
