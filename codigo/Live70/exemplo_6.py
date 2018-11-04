class NumeroPositivo:
    def __init__(self):
        self._n = None

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

    n = property(get_n, set_n, del_n)
