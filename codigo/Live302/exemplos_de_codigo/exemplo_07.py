class Contexto:

    def __enter__(self):
        print('Entrando no contexto')


    def __exit__(self, *args):
        print('Saindo no contexto')


with Contexto():
    print('Dentro do bloco!')
