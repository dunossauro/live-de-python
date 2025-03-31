# Padrão Prototype

- Live 283


## TOC

- Padrão Prototype
- Implementação clássica
- Copy
- Implementação pythonica

---

## Prototype

```python
d = {'a': 1}
d2 = d.copy()
```

## Implementação original

> original.py

## Copy

```python
import copy

copy.copy(objeto)  # razo
copy.deepcopy(objeto)  # profunda
copy.replace(objeto, attr=val)  # copia e troca attributos
```


> https://docs.python.org/3/whatsnew/3.13.html#copy - Referência de quem implementa replace.


### Protocolos de copy

- `__copy__`
- `__deepcopy__`
- `__replace__`

```python
def __replace__(self, **attrs):
    new = self.__class__.__new__(self.__class__)
	copy = self.__dict__.copy()

	new.__dict__ = copy | {
		key: value for key,value in attrs.items() if key in copy
	}

	return new
```

---


```python
def __replace__(self, **attrs):
	new = copy.deepcopy(self)

	new.__dict__ |= {
		key: value for key,value in attrs.items() if key in new.__dict__
	}

	return new
```



### ordem de descoberta de cópia

`__copy__` -> `__reduce_ex__` -> `__reduce__` -> `Raise`
`__deepcopy__` -> `__reduce_ex__` -> `__reduce__` -> `Raise`
`__replace__` - > `Raise`

https://docs.python.org/3/library/pickle.html#object.__reduce__
https://github.com/python/cpython/blob/main/Lib/copyreg.py#L103


## Implementação com python


deepcopy ...
