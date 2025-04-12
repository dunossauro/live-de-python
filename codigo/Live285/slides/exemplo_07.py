# /// script
# requires-python = ">=3.11"
# dependencies = ["pytest", "hypothesis"]
# ///
from hypothesis import given, example
from hypothesis.strategies import integers


def add(x: int, y: int) -> int:
    return x + y


@given(integers(), integers())
@example(x=1, y=1)
def test_add_comutativo(x, y):
    assert add(x, y) == add(y, x)


if __name__ == '__main__':
    import pytest

    pytest.main(['exemplo_07.py'])
