from typing import TypeIs, assert_type, reveal_type


def is_int(x: str | int) -> TypeIs[int]:
    return isinstance(x, int)


def func(val: str | int):
    if is_int(val):
        assert_type(val, int)
        return val
    else:
        assert_type(val, str)
        return val

a = func(1)
reveal_locals()
