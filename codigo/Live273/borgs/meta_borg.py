class MetaBorg(type):
    _state = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._state:
            cls._state[cls] = cls.__new__(cls)
        return cls._state[cls]


class C(metaclass=MetaBorg):
    ...
