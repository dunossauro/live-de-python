import sys
from logging import basicConfig, DEBUG, getLogger, Logger
from os import environ
from typing import Callable

import psutil

basicConfig(stream=sys.stdout, level=DEBUG)

TEMPERATURA_LIMITE = int(environ.get('TEMPERATURA_LIMITE', '40'))

logger = getLogger(__name__)


def cpu_temp() -> float:
    return psutil.sensors_temperatures()['coretemp'][0].current


class Container:
    def __init__(self):
        self._services = {}

    def register(self, name, dependency):
        self._services[name] = dependency

    def __getattr__(self, name):
        return self._services[name]


def ligar_cooler(container: Container) -> bool:
    if container.cpu_reader() >= container.max_temp:
        container.logger.info('Cooler ligado')
        return True

    container.logger.info('Cooler desligado')
    return False



if __name__ == '__main__':
    container = Container()
    container.register('cpu_reader', cpu_temp)
    container.register('max_temp', TEMPERATURA_LIMITE)
    container.register('logger', logger)

    ligar_cooler(container)


# ----------
# testes

import pytest


class FakeLogger:
    def __init__(self):
        self.messages = []

    def info(self, message):
        self.messages.append(message)


@pytest.mark.parametrize(
    ('temp', 'max_temp', 'msg', 'expected'),
    [
        (30, 40, 'Cooler desligado', False),
        (50, 40, 'Cooler ligado', True),
    ]
)
def test_decidir_estado_cooler(temp, max_temp, msg, expected):
    logger = FakeLogger()

    assert ligar_cooler(temp, max_temp, logger) == expected
    assert msg in logger.messages

