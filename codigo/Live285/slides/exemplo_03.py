# /// script
# requires-python = ">=3.11"
# dependencies = ["pytest", "faker"]
# ///
from faker import Faker

faker = Faker()


def add(x: int, y: int) -> int:
    return x + y


def test_add_comutativo():
    # exemplares
    x, y = faker.pyint(), faker.pyint()
    print(x, y)
    # Chamada do sut
    assert add(x, y) == add(y, x)


def test_add_neutro():
    # exemplares
    x, y = faker.pyint(), 0
    print(x, y)
    # Chamada do sut
    assert add(x, y) == x



if __name__ == '__main__':
    import pytest

    pytest.main(['exemplo_03.py'])
