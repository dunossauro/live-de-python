from itertools import count
from os.path import exists


class SaveAnother:
    counter = count(0)

    def __init__(self, file: str):
        self.file = file
        self.mode = 'w'
        self.obj = None

    def __enter__(self):
        if exists(self.file):
            file_name = '{}{}'.format(self.file,
                                      next(self.counter))
            self.obj = open(file_name, self.mode)
            return self.obj
        self.obj = open(self.file, self.mode)
        return self.obj

    def __exit__(self, type, value, traceback):
        print('Type: {} - Value: {} - Traceback: {}'.format(
            type, value, traceback))
        self.obj.close()
