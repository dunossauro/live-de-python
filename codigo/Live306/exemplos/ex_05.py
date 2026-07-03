import sys
from logging import basicConfig, DEBUG, getLogger
from os import environ
from typing import Callable

import psutil

basicConfig(stream=sys.stdout, level=DEBUG)
logger = getLogger(__name__)

TEMPERATURA_LIMITE = int(environ.get('TEMPERATURA_LIMITE', '40'))


def cpu_temp() -> float:
    return psutil.sensors_temperatures()['coretemp'][0].current


def ligar_cooler(
    cpu_temp_fn: Callable[[], float] = cpu_temp,  # DI
    max_temp: int = TEMPERATURA_LIMITE,           # Passagem de valores
) -> bool:
    temperatura_atual = cpu_temp_fn()
    if temperatura_atual >= TEMPERATURA_LIMITE:
        logger.info(f'Cooler ligado | TEMP {temperatura_atual}')
        return True

    logger.info(f'Cooler desligado |  TEMP {temperatura_atual}')
    return False


if __name__ == '__main__':
    ligar_cooler(cpu_temp)


# ----

# Testes
import pytest


@pytest.mark.parametrize(
    ('func', 'limit', 'expected'),
    [
        (lambda: 30, 40, False),
        (lambda: 30, 20, False),
        (lambda: 50, 40, True),
    ],
)
def test_ligar_cooler(func, limit, expected):
    result = ligar_cooler(func, limit)
    assert expected == result

