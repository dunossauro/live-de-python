# O que há de novo no python 3.12?

## Melhorias gerais

### Melhoria nas mensagens de erro

As melhorias em mensagens de erro vem acontecendo desde a versão 3.10.

Na versão 3.10 ganhamos funcionalidades para identificar a posição do erro na expressão para:

- `SintaxError`
- `IndentationError`
- `AttributeError`
- `NameError`

Agora na 3.12 além de melhoria nos erros já citados, também ganhamos o `importError` com mensagens melhores e algumas sugestões de nomes na biblioteca padrão.

Sugestões da biblioteca padrão:

```py
# 3.11
Traceback (most recent call last):
  File "/home/dunossauro/live_novidades/erros.py", line 1, in <module>
    @dataclasses.dataclass
     ^^^^^^^^^^^
NameError: name 'dataclasses' is not defined

# 3.12
Traceback (most recent call last):
  File "/home/dunossauro/live_novidades/erros.py", line 1, in <module>
    @dataclasses.dataclass
     ^^^^^^^^^^^
NameError: name 'dataclasses' is not defined. Did you forget to import 'dataclasses'?
```

Sugestões de coisas contidas nas bibliotecas:

```python
# 3.11
Traceback (most recent call last):
  File "/home/dunossauro/live_novidades/erros.py", line 5, in <module>
    from itertools import islici
ImportError: cannot import name 'islici' from 'itertools' (unknown location)

# 3.12
Traceback (most recent call last):
  File "/home/dunossauro/live_novidades/erros.py", line 5, in <module>
    from itertools import islici
ImportError: cannot import name 'islici' from 'itertools' (unknown location). Did you mean: 'islice'?
```

### Compreensões

Compreensões ganharam %11 de performance; Agora elas rodam no mesmo frame que o código que a chamou, anteriormente eram como chamadas de funções. Agora elas tem acesso ao escopo e as variáveis desse escopo:

```python
# Código
a = 7
print([locals() for x in [1]])
```

Execução:

```python
# 3.11
[{'.0': <tuple_iterator object at 0x7f6548dba470>, 'x': 1}]

# 3.12
[{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f6f613fc710>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/dunossauro/live_novidades/erros.py', '__cached__': None, 'a': 7, 'x': 1}]
```


## Bibliotecas
Inclusão de funcionalidades nas bibliotecas padrões

### pdb

Variáveis globais e temporárias que não interferem no frame nem na stack

```python
>>> import pdb
>>> pdb.set_trace()
>>> $a = 10
>>> $a
10
```

### Itertools

Itertools agora conta com uma nova função chamada `batched`, ela corta um iterável em pedaços menores

```python
from itertools import batched

batched([1, 2, 3, 4, 5], 2)
# (1, 2), (3, 4), (5,)
```

### Math

Agora podemos calcular o somatório do produto entre dois iteráveis:

```python
from math import sumprod


sumprod([1, 2, 3], [1, 2, 3])  # 14


# (1 * 1) + (2 * 2) + (3 * 3)
```

### Tempfile

Melhorias gerais

#### NamedTemporaryFile

Agora conta com um parâmetro `delete_on_close`. Agora o arquivo pode ser mantido após a finalização do gerenciador de contexto:

```python
with tempfile.TemporaryFile(delete_on_close=False) as fp:

   fp.write(b'Hello world!')

   fp.close()
```

#### mkdtemp

Agora sempre provê caminhos absolutos mesmo que `dir` seja relativo

```python
>>> from tempfile import mkdtemp

# 3.11
>>> mkdtemp(dir='.')
'./tmptm_w0uj4'

# 3.12
>>> mkdtemp(dir='.')
'/home/dunossauro/tmpx8zd6fln'
```

### Typing

Diversas melhorias foram implementadas na biblioteca

#### Checagem de protocolos em runtime

Agora protocolos com `runtime_checkable` podem ser checador dinamicamente por `isinstance`:


```
>>> from typing import Protocol, runtime_checkable

>>> @runtime_checkable
... class HasX(Protocol):
...     x = 1


>>> class Foo: ...

>>> f = Foo()

>>> isinstance(f, HasX)
False

>>> f.x = 1

>>> isinstance(f, HasX)
True

>>> HasX.y = 2

>>> isinstance(f, HasX)
True
```


#### Anotação para sobrescrita de método

```python
from typing import override

class Base:
    def get_color(self) -> str:
        return "blue"

class GoodChild(Base):
    @override  # ok: overrides Base.get_color
    def get_color(self) -> str:
        return "yellow"

class BadChild(Base):
    @override  # type checker error: does not override Base.get_color
    def get_colour(self) -> str:
        return "red"
```

#### Anotação de tipos para `kwargs`

Agora você pode anotar tipos para desempacotamento de argumentos nomeados usando `TypedDict` e `Unpack`:

```python
from typing import TypedDict, Unpack

class Movie(TypedDict):
  name: str
  year: int

def foo(**kwargs: Unpack[Movie]): ...
```


## CLIs

Novas interfaces de comando para serem chamadas com `-m` e funcionalidades para CLIs já existentes.

### SQLite3

Agora o shell do sqlite pode ser chamado via CLI do python:

```bash
python -m sqlite arquivo.db
```

### UUIDs

Agora podemos gerar UUID direto pelo CLI. Por padrão é 4, os uuid 2 e 5 precisam de name e namespace:

```bash
python -m uuid -u uuid4
11cb7757-fb95-4af3-930e-f705d96974f5


python -m uuid -u uuid1
93094c74-63a9-11ee-8325-48ad9a89a599


python -m uuid
df9ff1f0-aa27-4c62-bb70-84bcc4f80aee

python -m uuid -u uuid3 -n @dns -N dunossauro.com
28d8df77-5265-3bd1-8a41-6faa311be89b
```


### Unittest

Agora o unittest tem como medir a duração individual de testes. Isso pode ser usado com a flag `--durations`. Durations precisa receber um parâmetro que é a quantidade de testes que ele vai elencar dos mais lentos.

```bash
$ python -m unittest exemplo_unittest.py --durations=3
```

Nesse exemplo ele elencará os 3 testes mais lentos. O resultado:
```bash
.....
Slowest test durations
----------------------------------------------------------------------
5.000s     test_long_long (exemplo_unittest.TestExample.test_long_long)
3.000s     test_long (exemplo_unittest.TestExample.test_long)
2.000s     test_mid_long (exemplo_unittest.TestExample.test_mid_long)

----------------------------------------------------------------------
Ran 5 tests in 11.101s

OK
```

Podemos ver a duração de todos os testes usando `--durations=0` e a flag de verbose `-v`:

```bash
python -m unittest exemplo_unittest.py --durations=0 -v
test_long (exemplo_unittest.TestExample.test_long) ... ok
test_long_long (exemplo_unittest.TestExample.test_long_long) ... ok
test_mid (exemplo_unittest.TestExample.test_mid) ... ok
test_mid_long (exemplo_unittest.TestExample.test_mid_long) ... ok
test_short (exemplo_unittest.TestExample.test_short) ... ok

Slowest test durations
----------------------------------------------------------------------
5.000s     test_long_long (exemplo_unittest.TestExample.test_long_long)
3.000s     test_long (exemplo_unittest.TestExample.test_long)
2.000s     test_mid_long (exemplo_unittest.TestExample.test_mid_long)
1.000s     test_mid (exemplo_unittest.TestExample.test_mid)
0.100s     test_short (exemplo_unittest.TestExample.test_short)

----------------------------------------------------------------------
Ran 5 tests in 11.102s

OK
```

## Gramática

Só ouve uma mudança na gramática na versão 3.12 e ela é referente as `f-strings` que agora foram formalizadas:

...


## Sintaxe

Agora temos duas novas mudanças oriundas das anotações de tipos diretamente em como a linguagem é escrita. O uso da palavra reservada `type`, agora não só como função embutida, mas como instrução para definir apelidos para tipos e uma nova sintaxe para definição de generics parametrizados.

### A palavra reservada `type`

Quando as anotações foram inseridas na linguagem, caso tivéssemos um tipo que seria usado mais de uma vez, poderíamos criar um alias para ele, como uma variável "tradicional". A única premissa era que o nome deveria iniciar com letra maiúscula ([PEP-484](https://peps.python.org/pep-0484/#type-aliases), [PEP-8](https://peps.python.org/pep-0008/#type-variable-names)):

```python
MyDict = dict[str, str | float | list]
```

Na versão 3.10 do python foi um introduzida uma anotação específica e explícita para alias de tipos [PEP-613](https://peps.python.org/pep-0613/), o tipo `TypeAlias`, reduzindo a ambiguidade entre uma definição de variável e uma apelido de tipo:

```python
from typing import TypeAlias

MyDict: TypeAlias = dict[str, str | float | list]
```

Agora na versão 3.12 do Python ganhamos a instrução `type` com a [PEP-695]( https://peps.python.org/pep-0695/), para criação de apelidos.

```python
type MyDict = dict[str, str | float | list]
```

### A nova sintaxe para generics

Agora as variáveis de tipos agora podem ser definidas dentro do próprio namespace de declaração de forma lazy. Simplificando a utilização dos generics para anotações.

Sintaxe antiga:
```python
from typing import TypeVar, Generic

T = TypeVar('T')
def generic(x: T, y: T) -> T: ...


S = TypeVar('S', bound=complex)

class C(Generic[S]):
    ...

C[int]()
```

Sintaxe nova:
```python
def generic[T](x: T, y: T) -> T: ...

class C[S: complex]: ...

C[float]()
```

Se gostarem disso, podemos fazer uma live focada em generics, pois é um assunto bastante complexo!

## Menções honrosas

Mudanças e adições interessantes, que não vou me aprofundar nessa live!

### Random

Agora temos um valor randômico binomial para distribuições discretas. Retorna o número de sucessos para `n` tentativas independentes com a probabilidade de sucesso sendo `p`

```python
from random import binomialvariate

binomialvariate(n, p)
```

### Sys

Monitoração de baixo impacto com `sys.monitoring`. Mais informação na [PEP-669](https://peps.python.org/pep-0669/).

### Statistics

Agora `statistics.correlation`, usado para obter o coeficiente de correlação de Pearson, agora conta com o parâmetro `ranked`. Para obter o coeficiente de correlação de postos de Spearman.

```python
>>> from statistics import correlation

>>> qi = [106, 86, 100, 101, 99, 103, 97, 113, 112, 110]
>>> horas_de_tv = [7, 0, 27, 50, 28, 29, 20, 12, 6, 17]

>>> correlation(qi, horas_de_tv, method='ranked')
-0.17575757575757575

# método antigo, linear
>>> correlation(qi, horas_de_tv, method='linear')
-0.037601473846875934
```

### Subinterpretadores

A API C do python agora permite chamar N interpretadores dentro de outros interpretadores. Uma forma de burlar o GIL.

Teremos uma live focada só nisso com o @JSBueno
