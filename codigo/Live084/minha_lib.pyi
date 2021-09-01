from typing import Union


def div(x: int, y: Union[float, int]) -> float:
    ...


def mult(x: Union[str, int], y: int) -> Union[str, int]:
    ...


def soma(
    x: Union[complex, str, int, float], y: Union[complex, str, int, float]
) -> Union[complex, str, int, float]:
    ...


def sub(x: Union[float, int], y: Union[float, int]) -> Union[float, int]:
    ...
