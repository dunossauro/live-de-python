import sys
from logging import basicConfig, DEBUG, getLogger, Logger
from os import environ

import psutil

basicConfig(stream=sys.stdout, level=DEBUG)
logger = getLogger(__name__)

TEMPERATURA_LIMITE = int(environ.get('TEMPERATURA_LIMITE', '40'))


def cpu_temp() -> float:
    return psutil.sensors_temperatures()['coretemp'][0].current


def ligar_cooler(  # Passagem de valores
    cpu_temp: float,
    max_temp: int = TEMPERATURA_LIMITE,
    logger: Logger = logger,
) -> bool:
    if cpu_temp >= max_temp:
        logger.info("Cooler ligado")
        return True

    logger.info("Cooler desligado")
    return False


if __name__ == '__main__':
    temp = cpu_temp()
    ligar_cooler(temp)


# ----

# Testes
import pytest


class FakeLogger:
    def __init__(self):
        self.messages = []

    def info(self, message):
        self.messages.append(message)


@pytest.mark.parametrize(
    ('temp', 'max_temp', 'msg', 'expected'),
    [(30, 40, 'Cooler desligado', False), (50, 40, 'Cooler ligado', True)]
)
def test_decidir_estado_cooler(temp, max_temp, msg, expected):
    logger = FakeLogger()

    assert ligar_cooler(temp, max_temp, logger) == expected
    assert msg in logger.messages
