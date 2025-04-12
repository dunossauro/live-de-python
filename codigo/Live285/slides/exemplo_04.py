# /// script
# requires-python = ">=3.11"
# dependencies = ["pytest", "hypothesis"]
# ///
from hypothesis import given


def add(x: int, y: int) -> int:
    return x + y


@given(...)
def test_add_comutativo(x: int, y: int):
    print(x, y)
    assert add(x, y) == add(y, x)


if __name__ == '__main__':
    import pytest

    pytest.main(['-s', 'exemplo_04.py'])
