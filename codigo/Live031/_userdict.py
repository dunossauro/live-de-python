from collections import UserDict


class MyDict(UserDict):
    def __lshift__(self, value):
        self.data['last'] = value
    def __setitem__(self, pos, value):
        super().__setitem__(pos, value * 2)
