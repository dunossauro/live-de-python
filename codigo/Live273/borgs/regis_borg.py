class RegisBorg:
    _instances = {}

    def __init__(self, context):
        if not context in self._instances:
            self._instances[context] = self.__dict__
        else:
            self.__dict__ = self._instances[context]
