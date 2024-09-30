class MetaRegisBorg(type):
    _state = {}

    def __call__(cls, context, *args, **kwargs):
        if (cls, context) not in cls._state:
            cls._state[(cls, context)] = cls.__new__(cls)
        return cls._state[(cls, context)]
