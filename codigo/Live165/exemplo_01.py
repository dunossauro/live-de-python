from pydantic import validate_arguments


@validate_arguments
def soma(x: int, y: int):
    return x + y
