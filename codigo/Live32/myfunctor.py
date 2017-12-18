from myABC import Functor


class MyFunctor(Functor):
    def __init__(self, list_):
        self._d = list_

    def __getitem__(self, pos):
        return self._d[pos]

    def __len__(self):
        return len(self._d)

    def fmap(self, function):
        return MyFunctor([function(x) for x in self._d])

    def __repr__(self):
        return '{}'.format(self._d)

    def __mul__(self, functor):
        """ver em oslash ou pymonad."""
        # if isinstance(functor, Functor):
        #     return list(map(lambda value:  [func(value) for func in functor],
        #                     self._d))
        pass
