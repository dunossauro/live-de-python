from abc import ABC, abstractmethod


class Functor(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __getitem__(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def fmap(self, function):
        pass
