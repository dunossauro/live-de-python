from mamba import describe, it, context
from expects import expect, contain

def concat(x, y):
    return x + y


sanduiche = 'sanduiche com queijo'

with describe(sanduiche) as self:
    with it('tem queijo'):
        expect(sanduiche).to(contain('queijo'))

    with it('é um sanduiche'):
        expect(sanduiche).to(contain('sanduiche'))

    with context('Sanduiche vegano'):
        with it('Não tem Bacon'):
            expect(sanduiche).to_not(contain('bacon'))
