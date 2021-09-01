from builtins import property as _property, tuple as _tuple
from operator import itemgetter as _itemgetter
from collections import OrderedDict


class TIPO(tuple):
    'TIPO(VALOR,)'

    __slots__ = ()

    _fields = ('VALOR',)


    def __new__(_cls, VALOR,):
        'Create new instance of TIPO(VALOR,)'
        return _tuple.__new__(_cls, (VALOR,))

    @classmethod
    def _make(cls, iterable, new=tuple.__new__, len=len):
        'Make a new TIPO object from a sequence or iterable'
        result = new(cls, iterable)
        if len(result) != 1:
            raise TypeError('Expected 1 arguments, got %d' % len(result))
        return result

   def _replace(_self, **kwds):
        'Return a new TIPO object replacing specified fields with new values'
        result = _self._make(map(kwds.pop, ('VALOR',), _self))
        if kwds:
            raise ValueError('Got unexpected field names: %r' % list(kwds))
        return result

    def __repr__(self):
        'Return a nicely formatted representation string'
        return self.__class__.__name__ + '(VALOR=%r)' % self


    def _asdict(self):
        'Return a new OrderedDict which maps field names to their values.'
        return OrderedDict(zip(self._fields, self))

    def __getnewargs__(self):
        'Return self as a plain tuple.  Used by copy and pickle.'
        return tuple(self)

    VALOR = _property(_itemgetter(0), doc='Alias for field number 0')
