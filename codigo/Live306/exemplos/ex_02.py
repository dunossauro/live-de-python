import sys
from logging import basicConfig, DEBUG, getLogger

import psutil

basicConfig(stream=sys.stdout, level=DEBUG)
logger = getLogger(__name__)

TEMPERATURA_LIMITE = 40


def cpu_temp() -> float:
    return psutil.sensors_temperatures()['coretemp'][0].current


def ligar_cooler(temperatura_atual: float) -> bool:
    if temperatura_atual >= TEMPERATURA_LIMITE:
        logger.info(f'Cooler ligado | TEMP {temperatura_atual}')
        return True

    logger.info(f'Cooler desligado |  TEMP {temperatura_atual}')
    return False


if __name__ == '__main__':
    temp = cpu_temp()
    ligar_cooler(temp)


# ----

# Testes
import pytest


@pytest.mark.parametrize(  # Arrange
    ('temp', 'expected_result'),
    [(30, False), (50, True)],
    ids=['Temperatura baixa', 'Temperatura alta']
)
def test_ligar_cooler(temp, expected_result):
    result = ligar_cooler(temp)       # Act
    assert expected_result == result  # Assert

