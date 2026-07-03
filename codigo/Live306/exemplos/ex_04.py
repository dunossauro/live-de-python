import sys
from logging import basicConfig, DEBUG, getLogger

import psutil

basicConfig(stream=sys.stdout, level=DEBUG)
logger = getLogger(__name__)

TEMPERATURA_LIMITE = 40


def cpu_temp() -> float:
    return psutil.sensors_temperatures()['coretemp'][0].current


def ligar_cooler() -> bool:
    temperatura_atual = cpu_temp()

    if temperatura_atual >= TEMPERATURA_LIMITE:
        logger.info(f'Cooler ligado | TEMP {temperatura_atual}')
        return True

    logger.info(f'Cooler desligado |  TEMP {temperatura_atual}')
    return False


if __name__ == '__main__':
    ligar_cooler()


# ----

# Testes
import pytest


@pytest.mark.parametrize(
    ('func', 'expected'),
    [(lambda: 30, False), (lambda: 50, True)],
    ids=['Temperatura baixa', 'Temperatura alta']
)
def test_ligar_cooler(
    monkeypatch, func, expected
):
    # monkeypatch.setattr('modulo.cpu_temp', func)
    # Hack pra ficar no mesmo arquivo
    monkeypatch.setattr(sys.modules[__name__], 'cpu_temp', func)

    result = ligar_cooler()
    assert expected == result

