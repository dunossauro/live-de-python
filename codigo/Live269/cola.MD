# Sistema de imports!


## Namespaces
> Indicação da live de namespaces (https://youtu.be/nWmPEgTwGMM)

### `globals()`


```python
>>> globals()
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__cached__': None,
 '__doc__': None,
 '__file__': '/home/dunossauro/Live269/aqui.py',
 '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x732b2bc91f30>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None}
```

```python
a = 1
b = 2
c = 3
d = 4
```

```python
a = 10

def xpto():
    a = 1
    print(locals())
```

### `locals()`


## Imports I

```python
import functools
globals()
```

### import <>
> https://docs.python.org/3/reference/import.html

#### types.Module

```python
>>> import modulo
>>> type(modulo)
<class 'module'>
```


### from <> import <>

### Imports relativos


## Módulos

```
.
├── aqui.py
├── modulo.cpython-312-x86_64-linux-gnu.so
├── modulo.py
├── pacote
│  ├── __init__.py
│  ├── modulo.py
│  ├── subpacote
│  │  ├── __init__.py
│  │  └── submodulo.py
│  └── subpacote_namespace
│     └── submodulo.py
└── pacote_namespace
   ├── modulo.py
   └── subpacote
      └── __init__.py
```

### Arquivos .py (modulos)

```python
>>> import modulo
>>> modulo.soma(1, 1)
2
```
### Arquivos .pyc (compilados)


```
.
├── __pycache__
│  └── modulo.cpython-313.pyc
```

> Como o compilado é gerado? https://youtu.be/pxfZTAJDipY


### Diretórios com __init__ (pacotes)

> Querem uma live sobre módulos?!

```
├── pacote
│  ├── __init__.py
│  ├── modulo.py
```

```python
>>> from pacote.modulo import soma
'To no pacote'
>>> soma(1, 1)
2
```

### Diretórios sem __init__ (pacotes de namespace)


### Extensões em C (.so)

> mypyc

### Pacote "distribuído"

```python
from opentelemetry.A import a
from opentelemetry.B import b  # outra lib!
```

## Imports II

### __import__

https://docs.python.org/3/library/functions.html#import__

### importlib

https://docs.python.org/3/library/importlib.html


## Fundo do poço
- loaders
- finders
- zip
- PYTHONPATH / PYTHONHOME
- sys.path
- pyO3
- frozen
- bytecode
https://docs.python.org/3/library/dis.html#opcode-IMPORT_NAME




# Referências

- PEP 382: https://peps.python.org/pep-0382/
- PEP 402: https://peps.python.org/pep-0402/
- PEP 420: https://peps.python.org/pep-0420/
