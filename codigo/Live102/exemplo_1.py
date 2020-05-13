

from mamba import describe, it

sanduiche = 'sanduiche com queijo'


with describe(sanduiche) as self:
    with it('tem queijo'):
        assert 'queijo' in sanduiche

    with it('é um sanduiche'):
        assert 'sanduiche' in sanduiche
