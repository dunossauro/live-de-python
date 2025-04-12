# /// script
# requires-python = ">=3.11"
# dependencies = ["pytest"]
# ///
def add(x: int, y: int) -> int:
    return x + y


def test_add():
    # Arrange: Organização dos dados para o teste
    x, y = 1, 1
    esperado = 2

    # Chamada do SUT
    resultado = add(x, y)

    # Assert
    assert resultado == esperado


if __name__ == '__main__':
    import pytest

    pytest.main(['exemplo_00.py'])
