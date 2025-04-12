# /// script
# requires-python = ">=3.11"
# dependencies = ["pytest"]
# ///
from pytest import mark


def add(x: int, y: int) -> int:
    return x + y


@mark.parametrize('x,y,esperado', [(1, 1, 2), (2, 2, 4), (5, 5, 10)])
def test_add(x, y, esperado):
    # Chamada do SUT
    resultado = add(x, y)

    # Assert
    assert resultado == esperado

if __name__ == '__main__':
    import pytest

    pytest.main(['exemplo_01.py'])
