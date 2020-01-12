from mamba import description, it

with description('Um tópico') as self:
    with it('Acontece alguma coisa e eu posso checar'):
        valor = 'Live'
        outro = 'Python'

        assert valor != outro
