from unicodedata import normalize


def normaliza(*palavras):
    saida = []

    for palavra in palavras:
        normalizado = normalize('NFKD', palavra)
        normalizada = normalizado.encode('ASCII', 'ignore').decode('ASCII')
        saida.append(normalizada)

    return saida


print(normaliza('Érico', 'Sabiá', 'João'))
# ['Erico', 'Sabia', 'Joao']


def normaliza2(*palavras):

    def ajudante(palavra):
        normalizado = normalize('NFKD', palavra)
        return normalizado.encode('ASCII', 'ignore').decode('ASCII')

    return [ajudante(palavra) for palavra in palavras]


print(normaliza2('Érico', 'Sabiá', 'João'))
# ['Erico', 'Sabia', 'Joao']
