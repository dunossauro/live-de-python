class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state
