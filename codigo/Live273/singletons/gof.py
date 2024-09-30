from __future__ import annotations


class Singleton:
    instance: Singleton

    @classmethod
    def get_instance(cls) -> Singleton:
        if not hasattr(cls, 'instance'):
            cls.instance = Singleton()
        return cls.instance
