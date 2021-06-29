from pytest import mark
from app.calc import soma


def test_soma_1_1_retona_2():
    assert soma(1, 1) == 2


@mark.slow
def test_soma_2_2_retorna_4():
    from time import sleep

    sleep(5)

    assert soma(2, 2) == 4
