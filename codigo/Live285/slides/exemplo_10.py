# /// script
# requires-python = ">=3.11"
# dependencies = ["pytest", "hypothesis"]
# ///
from hypothesis import given
from hypothesis.strategies import lists, text


def concat(x: list[str], y: list[str]) -> list[str]:
    return x + y


@given(lists(text()), lists(text()))
def test_concat_size(x, y):
    result = concat(x, y)

    assert len(result) == len(x) + len(y)


if __name__ == '__main__':
    import pytest

    pytest.main(['exemplo_10.py'])
