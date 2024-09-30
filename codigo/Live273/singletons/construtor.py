from __future__ import annotations


class Singleton:
    instance: Singleton

    def __new__(cls) -> Singleton:
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance
