# /// script
# requires-python = ">=3.11"
# dependencies = ["pytest", "hypothesis"]
# ///
from hypothesis import Verbosity, example, given, settings


def add(x: int, y: int) -> int:
    return x + y


@given(...)
@example(x=-1000, y=17)
@settings(max_examples=50, verbosity=Verbosity.verbose)
def test_add_comutativo(x: int, y: int):
    assert add(x, y) == add(y, x)


if __name__ == '__main__':
    import pytest

    pytest.main(['-s', 'exemplo_05.py'])
