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


def ligar_cooler(cpu_temp_fn: Callable[[], float] = cpu_temp) -> bool:
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
        (lambda: 30, '40', False),
        (lambda: 30, '20', False),
        (lambda: 50, '40', True),
    ],
)
def test_ligar_cooler(monkeypatch, func, limit, expected):
    # Aqui alteramos a veriável de ambiente
    monkeypatch.setenv('TEMPERATURA_LIMITE', limit)

    result = ligar_cooler(func)
    assert expected == result



def test_log_quando_liga(caplog, monkeypatch):
    caplog.set_level(DEBUG)
    monkeypatch.setenv('TEMPERATURA_LIMITE', '5')
    
    ligar_cooler(lambda: 10)

    assert 'Cooler desligado' in caplog.text
