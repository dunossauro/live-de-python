"""
Nomemclatura da PEP:
 - Subgerador: O que será consumido por yield from
 - Delegante: O gerador que terá o yield from
 - Cliente ou Chamador: Quem chama ou é servido pelo gerador delegante

Esquema:

Cliente -> Delegante -> Subgerador

O subgerador é uma corrotina tradicional, porém agora ela pode ser parada com Return. Ou seja, sua condição de parada é dada por um return.

No nosso caso a corrotina `acumular` é uma corrotina tradicional, porém agora ela conta com return, onde pode repassar ao delegante o resultado final da operação.

O delegante por sua vez é quem repassa a corrotina `acumular` ao cliente, para que ele possa manipular o subgerador. Quando o subgerador "acaba" ele cria um novo subgerador para o cliente

O cliente fica responsável somente por alimentar o subgerador e o finalizar
"""


def acumular():
    """
    Toda vez que yield recebe um valor, adiciona ao contador.

    contador = 0
    acumular.send(10)  # contador = 10
    acumular.send(10)  # contador = 20

    Quando receber None, retorna o valor final da contagem
    acumular.send(None)  # 20

    NOTE: Esse é o subgerador
    """
    contador = 0
    print('Inicializei `acumular`')
    while True:
        valor = yield  # Recebe um valor
        print(f'`acumular` recebeu valor={str(valor)}')

        if valor is None:
            # Se for None, retorna o valor final da contagem
            print('Finalizei `acumular`')
            return contador

        contador += valor  # Caso não seja nulo acumula o valor
        print(f'`acumular` - Valor total: {contador=}')


def agregador_de_contadores(contadores):
    """
    Agregador = gather.

    Quando iniciada retorna a corotina `acumular`

    Quando a corrotina retonar um valor irá fazer um append em `contadores`
    E então retornara uma nova "instancia" de `acumular`

    NOTE: Esse é o gerador delegante
    """
    print('Iniciei `agregador_de_contadores`')
    while True:
        print('Deleguei para `acumular`')
        contador = yield from acumular()
        contadores.append(contador)
        print(f'Valor Atual de {contadores=}')


"""
Cliente -> Delegante -> Subgerador
"""

# Cliente
contadores = []
agregador = agregador_de_contadores(contadores)  # Inicia o gerador delegante
next(agregador)  # Preparação

for i in range(4):
    # 0 + 1 + 2 + 3
    agregador.send(i)  # Enviando valores para `acumular`

agregador.send(None)  # 6

# Finaliza a corrotina `acumular`, com isso `agregador` faz insere o valor final em `contadores`

print(contadores)  # [6]
# Fim do Cliente


for i in range(5):
    # 0 + 1 + 2 + 3 + 4
    agregador.send(i)

agregador.send(None)  # 10


for i in range(10):
    # 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
    agregador.send(i)

agregador.send(None)  # 45

print(contadores)  # [6, 10, 45]
