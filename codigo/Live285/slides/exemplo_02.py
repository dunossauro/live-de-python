# /// script
# requires-python = ">=3.11"
# dependencies = ["pytest"]
# ///
def add(x: int, y: int) -> int:
    return x + y


def test_add_comutativo():
    # exemplares
    x, y = 3, 2
    # Chamada do sut
    assert add(x, y) == add(y, x)


if __name__ == '__main__':
    import pytest

    pytest.main(['exemplo_02.py'])
