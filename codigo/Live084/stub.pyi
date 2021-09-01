from typing import Union


def div(x: int, y: int) -> float:
    ...


def mult(x: Union[str, int], y: int) -> Union[str, int]:
    ...


def soma(
    x: Union[str, int, float], y: Union[str, int, float]
) -> Union[str, int, float]:
    ...


def sub(x: Union[float, int], y: Union[float, int]) -> Union[float, int]:
    ...
