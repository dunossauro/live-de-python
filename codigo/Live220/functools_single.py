from functools import singledispatch
from typing import Union


@singledispatch
def dispatch(arg):
    return 'Default'


@dispatch.register
def _(arg: Union[int, str]):
    return f'Int ou String {arg}'


@dispatch.register
def _(arg: float | list):
    return f'Float ou Lista {arg}'


print(dispatch(1))
print(dispatch('1'))
print(dispatch(1.0))
print(dispatch(['1']))
