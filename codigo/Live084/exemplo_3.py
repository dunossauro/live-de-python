from typing import Callable, Sequence, Generator, Union, List, Dict, Tuple

Alias = Union[List[int], Tuple[int, int, int], Dict[int, str]]


def soma_1(x: int) -> int:
    return x + 1


def xpto(x: str) -> str:
    return ''


# def mymap(f: Callable, l: Dict[int, str]) -> Generator:
def mymap(
    f: Callable[[int], int],
    l: Alias
) -> Generator:
    return (f(x) for x in l)


mymap(soma_1, [1, 2, 3])
# mymap(xpto, [1, 2, 3])  # error
mymap(soma_1, (1, 2, 3))
mymap(soma_1, {1: 'a', 2: 'b'})
