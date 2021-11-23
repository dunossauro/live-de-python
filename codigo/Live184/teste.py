import pytest  # noqa

from programa import altera_linha


def test_altera_linha():
    result = altera_linha("uma linha")
    assert result == "linha uma\n"
