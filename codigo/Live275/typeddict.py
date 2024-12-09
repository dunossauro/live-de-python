from typing import TypedDict, ReadOnly


class D(TypedDict):
    x: ReadOnly[int]
    y: int


d: D = {'x': 1, 'y': 2}
d['x'] = 10
# error: Could not assign item in TypedDict
#    "x" is a read-only key in "D"
