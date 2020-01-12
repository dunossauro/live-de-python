

from expects import expect, contain, be_an


class Bacon:
    ...


sanduiche = 'sanduiche com queijo'

expect(sanduiche).to(contain('queijo'))

expect(sanduiche).to_not(be_an(Bacon))
