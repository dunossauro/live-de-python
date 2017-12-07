from collections import UserString


class MyString(UserString):
    def __iter__(self):
        return iter(self.data)

    def next(self):
        for x in self.data:
            yield x
