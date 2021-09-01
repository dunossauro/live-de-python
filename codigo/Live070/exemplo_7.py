class Descritor:
    def __init__(self, obj, set=None, get=None, delete=None):
        self.obj = obj
        self.set = set
        self.get = get
        self.delete = delete

    def __set__(self, obj, val):
        print('Estou setando algo')
        self.obj = val

    def __get__(self, obj, tipo=None):
        print('Estou pegango algo')
        return self.obj

    def __delete__(self, obj):
        print('Estou deletando algo')
        del self.obj

    def __repr__(self):
        return self.obj


class NumeroPositivo:
    _n = None

    def get_n(self):
        print('get')
        return self._n

    def set_n(self, val):
        print('set')
        if val < 1:
            ...
        else:
            self._n = val

    def del_n(self):
        print('del')
        del self._n

    n = Descritor(_n)
