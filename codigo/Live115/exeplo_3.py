from generic import generic

@generic
def paul(evento):
    print(f'{evento}')


@paul.when(lambda evento: evento['cor'] == 'amarelo')
def amarelo(evento):
    print(evento)


@paul.when(lambda evento: 'amarelo' in evento['msg'])
def amarelo(evento):
    print(evento)
