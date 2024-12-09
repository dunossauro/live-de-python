# O que há de novo 3.13

- Fim do suporte de segurança da 3.8

## Melhoria nas mensagens de erro!

### Cores!
Controle por meio de variáveis de ambiente:

- `PYTHON_COLORS=?` 0 sem cores, 1 com cores

> TODO: colocar prints

### Erros melhores

- Erro quando o arquivo tem o mesmo nome da biblioteca padrão:

```python
# functools.py
import functools

g
@functools.cache
def xpto(): ...
```

```python
python functools.py 
Traceback (most recent call last):
  File "/home/dunossauro/live_313/functools.py", line 1, in <module>
    import functools
  File "/home/dunossauro/live_313/functools.py", line 4, in <module>
    @functools.cache
AttributeError: module 'functools' has no attribute 'cache' (consider renaming '/home/dunossauro/live_313/functools.py' since it has the same name as the standard library module named 'functools' and the import system gives it precedence)
```

- Os mesmos erros também valem para bibliotecas externas:

```python
# pydantic.py
import pydantic


class Model(pydantic.BaseModel): ...
```

```python
python pydantic.py 
Traceback (most recent call last):
  File "/home/dunossauro/live_313/pydantic.py", line 1, in <module>
    import pydantic
  File "/home/dunossauro/live_313/pydantic.py", line 4, in <module>
    class Model(pydantic.BaseModel): ...
AttributeError: module 'pydantic' has no attribute 'BaseModel' (consider renaming '/home/dunossauro/live_313/pydantic.py' if it has the same name as a third-party module you intended to import)
```

- Sugestão de nomes de parâmetros:

```python
def xpto(batatinha_frita):
    ...


xpto(batatinhafrita=1)
```

```python
python erros_params.py 
Traceback (most recent call last):
  File "/home/dunossauro/live_313/erros_params.py", line 5, in <module>
    xpto(batatinhafrita=1)
TypeError: xpto() got an unexpected keyword argument 'batatinhafrita'. Did you mean 'batatinha_frita'?
```

## Novo shell interativo!

- Edição multilinha
- Atalhos:
  - F1: Ajuda
  - F2: Histórico
  - F3: Colar multilinha

## [WIP] CPython com threads livres

Post do nilo falando sobre a comparação de tempo:
https://blog.nilo.pro.br/posts/2024-10-08-python313/

Adicionando mais versões:
https://gist.github.com/dunossauro/afea7800f06d7bd1b23f8bff71bc74e1

### Como ver se a biblioteca tem suporte

As libs suportadas tem a tag de plataforma com o final `t`.

Por exemplo o pandas:

pandas        -2.2.3    -cp313       -cp313t   -musllinux_1_2_x86_64.whl

pedalboard-0.9.16-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (7.9 MB view hashes) 
{distribution}-{version}-{python tag}-{abi tag}-{platform tag}.whl

platform tags: https://packaging.python.org/en/latest/specifications/platform-compatibility-tags/#platform-compatibility-tags
Exemplo: https://pypi.org/project/pandas/#files

### Bibliotecas compatíveis

https://py-free-threading.github.io/tracking/

## [WIP] Um compilador just-in-time (JIT) experimental

### Interpretador adaptado especializado

Tier 2 (buscar a imagem usada na live do interpretador adaptativo)

#### Os diferentes tipos de tier 2

- Interpretador de tier 2
- Compilador JIT de tier 2

### Análise de desempenho
Cortes de áudio em um arquivo de ~01:30:00

3.12 - oficial
real	4m39,785s
user	3m43,800s
sys	1m6,059s

3.12 - Lib
real	4m42,347s
user	3m46,734s
sys	1m6,119s

3.13 - Lib
real	4m44,196s
user	3m47,766s
sys	1m6,099s

3.13 - lib/jit
real	4m43,121s
user	3m48,983s
sys	1m4,706s

## Definidas semânticas de mutação para `locals()`

```python
def f():
    x = 1
    sys._getframe().f_locals['x'] = 2
    print(x)
f()  # Agora retorna 2!
```

https://peps.python.org/pep-0667/

## Suporte para plataformas móveis

Android e iOS agora são tier 3 <3 <3 <3 <3

wasi agora é tier 2! :)

## Melhoria no tabanho da docstring armazenada

Agora as tabulações e espaços são removidos do .pyc

## Listagem de atributos estáticos

Agora os atributos criados em métodos são adicionados a `__static_attributes__`. Melhoria para checadores e também para autocomplete:

```python
class C:

    def xpto(self, val):
        self.val = val

>>> C.__static_attributes__
('a',)
```

## warnings (PEP 702)

Agora os avisos tem um decorador de `deprecated` que podem avisar o checador de tipos (ainda sem suporte no mypy e no pyright) que algo está deprecado. O aviso também é levantado em runtime:

```python
# dep.py
from warnings import deprecated


@deprecated('Atualiza essa paradinha!')
def xpto():
    ...


xpto()
```

```
python dep.py 
/home/dunossauro/live_313/dep.py:9: DeprecationWarning: Atualiza essa paradinha!
  xpto()
```


## Random agora tem CLI

```
python -m random 
usage: random.py [-h] [-c CHOICE [CHOICE ...] | -i N | -f N]
                 [input ...]

positional arguments:
  input                 if no options given, output depends on the input
                            string or multiple: same as --choice
                            integer: same as --integer
                            float: same as --float

options:
  -h, --help            show this help message and exit
  -c, --choice CHOICE [CHOICE ...]
                        print a random choice
  -i, --integer N       print a random integer between 1 and N inclusive
  -f, --float N         print a random floating-point number between 1 and N inclusive
```

## [WIP] Typing!

Novas adições no typing

### PEP-705 - TypedDict: Read-only items

```python
from typing import TypedDict, ReadOnly, Required, NotRequired


class D(TypedDict):
    x: ReadOnly[int]
    y: int
    z: Required[float]
	w: NotRequired[str]

d: D = {'x': 1, 'y': 2}
d['x'] = 10
# error: Could not assign item in TypedDict
#    "x" is a read-only key in "D"
```

### [TRAD] PEP 742 – Narrowing types with TypeIs

Alternativa ao `TypeGuard` para resolver alguns problemas:

Limitation 1: Type checkers are not allowed to narrow a type in the case where the type guard function returns False. This means the type is not narrowed in the negative (“else”) clause.

Limitation 2: Type checkers must use the TypeGuard return type if the type guard function returns True regardless of whether additional narrowing can be applied based on knowledge of the pre-narrowed type.

Para especificar o comportamento do `TypeIs`, vamos usar a seguinte terminologia:
- I = TypeIs de entrada
- R = TypeIs tipo de retorno
- A = Tipo do argumento que será passado para o afunilamento
- NP = Tipo afunilado (positivo; usando quando TypeIs retorna True)
- NN = Tipo afunilado (negativo; usando quando TypeIs retorna False)

```python
def narrower(x: I) -> TypeIs[R]: ...

def func1(val: A):
    if narrower(val):
        assert_type(val, NP)
    else:
        assert_type(val, NN)
```

Exemplo real:

```python
def is_int(x: str | int) -> TypeIs[int]:
    return insinstace(x, int)

def is_int(val: str | int):
    if narrower(val):
        assert_type(val, int)
    else:
        assert_type(val, str)
```

https://peps.python.org/pep-0724/ (Motivação)
https://peps.python.org/pep-0742/ (Resultado)


### PEP 696 – Type Defaults for Type Parameters 

```python
class C[T = str]:
    ...
```

ou

```python
from typing import TypeVar, Generic


T = TypeVar('T', default=str)


class C(Generic[T]):
    def __init__(self, val_1, val_2) -> None:
        self.val_1: T = val_1
        self.val_2: T = val_2


c = C[int](1, 2)
d = C('1', '2')

d.val_1.capitalize()
```

## Copy

Agora o módulo de `copy` tem uma nova função chamado `.repace` que cria um novo objeto trocando alguns atributos:

```python
import copy
from dataclasses import dataclass

@dataclass
class C:
    c: int = 10
    
>>> copy.replace(C(), c=20)
C(c=20)
```

Objetos suportados até agora:


- collections.namedtuple()
- dataclasses.dataclass
- datetime.datetime, datetime.date, datetime.time

Seus objetos podem suportar com o `__replace__`:

```python
class C:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __replace__(self, /, **changes):
        new_attrs = self.__dict__ | changes
        return C(**new_attrs)

    def __repr__(self):
        return f'C({self.__dict__})'
```

## [NF] PythonFinalizationError
## Documentação

Agora o código fonte da documentação também está traduzido:

https://docs.python.org/pt-br/3/whatsnew/3.13.html#other-language-changes
