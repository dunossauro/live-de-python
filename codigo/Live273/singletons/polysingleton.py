from functools import cache


@cache
class Singleton:
    def __init__(self, context=None):
        self.context = context
