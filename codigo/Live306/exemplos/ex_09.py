import sys
from logging import basicConfig, DEBUG, getLogger, Logger
from os import environ

import psutil

basicConfig(stream=sys.stdout, level=DEBUG)
logger = getLogger(__name__)

TEMPERATURA_LIMITE = int(environ.get('TEMPERATURA_LIMITE', '40'))


class Container:
    def __init__(self):
        self._services = {}

    def register(self, name, dependency):
        self._services[name] = dependency

    def __getattr__(self, name):
        return self._services[name]


def cpu_temp() -> float:
    return psutil.sensors_temperatures()['coretemp'][0].current

def ligar_cooler(container: Container) -> bool:
    if container.cpu_reader() >= container.max_temp:
        container.logger.info('Cooler ligado')
        return True

    container.logger.info('Cooler desligado')
    return False


if __name__ == '__main__':
    container = Container()
    container.register('cpu_reader', cpu_temp)
    container.register('max_temp', 40)
    container.register('logger', logger)
    ligar_cooler(container)


# testes

import pytest


class FakeLogger:
    def __init__(self):
        self.messages = []

    def info(self, message):
        self.messages.append(message)


@pytest.mark.parametrize(
    ('temperatura', 'limite', 'expected', 'log_message'),
    [
        (30, 40, False, 'Cooler desligado'),
        (50, 40, True, 'Cooler ligado'),
    ],
    ids=['Temperatura baixa', 'Temperatura alta']
)
def test_ligar_cooler(temperatura, limite, expected, log_message):
    # Arrange
    container = Container()
    container.register('cpu_reader', lambda: temperatura)
    container.register('max_temp', limite)

    fake_logger = FakeLogger()
    container.register('logger', fake_logger)

    # Act
    result = ligar_cooler(container)

    # Assert
    assert result is expected
    assert log_message in fake_logger.messages
