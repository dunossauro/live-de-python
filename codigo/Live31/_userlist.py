from collections import UserList


class MyList(UserList):
    def __add__(self, value):
        self.data.append(value)
    def __sub__(self, value):
        if value in self.data:
            self.data.remove(value)
        else:
            pass
