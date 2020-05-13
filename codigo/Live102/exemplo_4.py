from mamba import context, describe, it, _it
from expects import expect, equal
from unittest.mock import patch
from app import concatx


def concat(x, y):
    return x + y


with describe('Função de concatenar') as self:
    with context('Juntar coisas'):
        with it('Deve juntar strings'):
            expect(concat('a', 'a')).to(equal('aa'))

        with it('Deve juntar listar'):
            expect(concat([0], [1])).to(equal([0, 1]))

    with context('Somar coisas'):
        with it('Deve somar números inteiros'):
            expect(concat(0, 1)).to(equal(1))

    with context('mockar'):
        with it('Deve somar números inteiros'):
            with patch('app.concats', return_value=10) as xpto:
                expect(concatx(0, 1)).to(equal(10))
                xpto.assert_called()
