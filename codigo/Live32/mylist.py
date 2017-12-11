from collections.abc import MutableSequence


class MyList(MutableSequence):
    def __init__(self, list_):
        self._d = list(list_)

    def __getitem__(self, pos):
        """Outra é usando __iter__ e __next__."""
        return self._d[pos]

    def __delitem__(self, pos):
        del(self._d[pos])

    def __len__(self):
        return len(self._d)

    def __setitem__(self, pos, val):
        self._d[pos] = val

    def insert(self, pos, val):
        self._d.index(pos, val)

    def __repr__(self):
        return '{}'.format(self._d)
