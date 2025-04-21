# Módulos e pacotes

## Módulos

### Duders de módulos (pensar em uma tradução)

#### `__all__`

```python
def x(): ...
def y(): ...

__all__ = ['x']
```

#### `__version__`

```toml
[project]
name = 'pacote'
dynamic = ['version']
# pacote.__init__.__version__

[tool.setuptools.dynamic] # atributo do módulo
version = {attr = "pacote.__version__"}

[tool.hatch.version] # arquivo que contém o metadado
path = "pacote/__init__.py"

[build-system]
requires = ["setuptools >= 77.0.3"]
build-backend = "setuptools.build_meta"
```
#### `__author__`

Metadado para saber de quem é autoria do pacote:

```python
__author__ = 'Fausto, O mago!'
```

#### Customização de acesso de atributos (PEP 562)

###### `__getattr__`

```python
def __getattr__(name: str):
    """
    Hook de import: Customiza a chamada de um atributo de módulo

    __getattr__ será chamado se e somente se o nome não estiver no módulo.

    Se o nome não tiver um callback, levantar um `AttributeError`
    """
    raise AttributeError(f'{name} not found')
```

###### `__dir___`

```python
def x(): ...
def y(): ...

__all__ = ['x']


def __dir__():
    return __all__ + ['y']
```

## Pacotes

### Pacotes de namespaces (PEP 420)

```text
.
└── p_namespace
    └── modulo.py
```

```python
>>> from p_namespace.modulo import xpto
>>> xpto
<function xpto at 0x712aa1d87b00>
```

### Tornando seu pacote executável `__main__`

```python
print('Ihuuuuuuuuuuuuuuuuuu!')
```

```bash
python -m pacote  # chama __main__.py
Ihuuuuuuuuuuuuuuuuuu!
```

### Pacotes regulares

#### O odiado ou amado `__init__`

```text
.
└── pacote
    └── __init__.py
    └── modulo.py
```

```python
# __init__.py
print('batatinhas')
```

```python
>>> import pacote
batatinhas
```

## Links citados

- Live de escopos e namespaces: https://youtu.be/nWmPEgTwGMM
- Live do sistema de imports: https://youtu.be/a5R5dvim6TQ
- Live do pyproject: https://youtu.be/6p1HKaHrk0Y

## Referências

- PEP 8: https://peps.python.org/pep-0008/#module-level-dunder-names
- PEP 562: https://peps.python.org/pep-0562/
- PEP 420: https://peps.python.org/pep-0420/
- Modulos: https://docs.python.org/pt-br/3.13/tutorial/modules.html
- Pacotes: https://docs.python.org/pt-br/3.13/tutorial/modules.html#packages
- Every dunder method: https://www.pythonmorsels.com/every-dunder-method/
- Discuss: https://discuss.python.org/t/module-level-getattr-and-from-imports/32236/7

### Dynamic version
- packing: https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#version
- setuptools: https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html#dynamic-metadata
- hatch: https://hatch.pypa.io/1.12/version/#configuration

---

https://excalidraw.com/#json=DmdiodKrKwP-2vhA-zIT2,7SXuoFdbsw4-WKJrKmrDbQ
