# /// script
# requires-python = ">=3.11"
# dependencies = ["pytest", "hypothesis"]
# ///
from hypothesis import given
from hypothesis.strategies import integers


def add(x: int, y: int) -> int:
    return x + y


@given(integers(-100, 0), integers(0, 100))
def test_add_comutativo(x, y):
    print(x, y)
    assert add(x, y) == add(y, x)


if __name__ == '__main__':
    import pytest

    pytest.main(['exemplo_08.py'])
