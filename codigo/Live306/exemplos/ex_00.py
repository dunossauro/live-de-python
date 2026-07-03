import sys
from logging import basicConfig, DEBUG, getLogger

import psutil

basicConfig(stream=sys.stdout, level=DEBUG)
logger = getLogger(__name__)

TEMPERATURA_LIMITE = 40


def ligar_cooler() -> bool:
    temp_atual: float = psutil.sensors_temperatures()['coretemp'][0].current

    if temp_atual >= TEMPERATURA_LIMITE:
        logger.info(f'Cooler ligado | TEMP {temp_atual}')
        return True

    logger.info(f'Cooler desligado |  TEMP {temp_atual}')
    return False


if __name__ == '__main__':
    ligar_cooler()


# ----

# Testes

def test_ligar_cooler():
    expected_result = True            # Arrange
    result = ligar_cooler()      # Act - Chama o SUT
    assert expected_result == result  # Assert
