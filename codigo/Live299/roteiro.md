# Roteiro geral em tópicos

Gerais:
    - Melhoria nas mensagens de erro
    - Debug
        - Remoto
		- Asyncio
    - REPL
        - Destaque de sintaxe
    - Cores
        - Unittest
		- Json
		- Argparse
		- Calendar

Plataformas:
    - WASM: nível 3
	- Android e iOS

Bibliotecas:
    - pathlib
        - Copiar
		- Mover
	- uuid
    - PEP 784: adicionando Zstandard à biblioteca padrão
    - PEP 749: annotationlib

Sintaxe:
    - PEP 758: Except sem ()
	- PEP 765: não permitir return/break/continue que saia de um bloco finally
	- PEP 750: Template strings
	- PEP 749/649: Avaliando tipos tardiamente

Interpretador:
	- Um novo tipo de interpretador
    - PEP 734: múltiplos interpretadores na biblioteca padrão
    - PEP 779: Python com threads livres é oficialmente suportado
	- PEP 744: Versões binárias para o compilador experimental just-in-time


## [OK] Gerais

### Melhoria nas mensagens de erro

- Sugestões de palavras chave
- Erros de unpack
- Strings dentro de strings
- Erros com `as`
- Erros com hashables
- Prefixos incompatíveis de strings
- Estruturas de `if`
- Palavras chave após `else`

#### Sugestões para palavras chave

```python
>>> forr x in [1, 2, 3]:
  File "<python-input-1>", line 1
    forr x in [1, 2, 3]:
    ^^^^
SyntaxError: invalid syntax. Did you mean 'for'?
```

#### Erros de unpack

Antes só mostrava quanto eram esperados, mas não quantos vieram

```python
>>> a, b = 1, 2, 3
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    a, b = 1, 2, 3
    ^^^^
ValueError: too many values to unpack (expected 2, got 3)
```

#### Strings dentro de strings

```python
>>> "abc "teste" def"
  File "<python-input-0>", line 1
    "abc "teste" def"
          ^^^^^
SyntaxError: invalid syntax. Is this intended to be part of the string?
```

#### Prefixos de strings

```python
>>> bt''
  File "<python-input-3>", line 1
    bt''
    ^^
SyntaxError: 'b' and 't' prefixes are incompatible
```

### Debugger

#### Debugger remoto

permissões: https://docs.python.org/3.14/howto/remote_debugging.html#remote-debugging-attachment-protocol

```python
# xpto.py
from time import sleep

d = {}

while True:
    print('loop')
    print(f'{d=}')
    sleep(5)
```

```bash
ps aux | grep xpto.py
```

```bash
python -m pdb -p {processo}
```


#### Debugger asyncio

```python
# asyncio_debug_test.py
from asyncio import gather, run, sleep as asleep
from time import sleep

async def maybe():
    print('maybe')
    await asleep(10)


async def task(n):
    print(f'task start - {n}')
    if n % 2:
        await maybe()
    await asleep(10)
    print(f'task end - {n}')


async def main():
    while True:
        sleep(3)
        await gather(*[task(x) for x in range(10)])

run(main())
```

```bash
ps aux | grep xpto.py
```

```bash
python -m asyncio pstree {processo}
```


### REPL

Mostrar na TELA!


### Cores!

- Calendar
- Argparse
- json
- unittest

#### Calendar

```bash
python -m calendar
```

#### Argparse

```bash
python -m json.tool --help
```

#### json

```bash
python -m json.tool test.json
{
    "key": "value",
    "pei": true,
    "au": 7
}
```

## [REV] Plataforma

- WASM: Tier 3!
- Android: Tem build oficial (https://www.python.org/downloads/release/python-3140rc3/)
- iOS: ????


## [WIP] Bibliotecas

### pathlib

Copia

```python
>>> Path('test.json').copy('test2.json')
Path('test2.json')
```

Move

```python
Path('test.json').move('test2.json')
```


### UUID

Suporte para uuids 6, 7 e 8

```bash
python -m uuid -u uuid8
1f2eaa8f-a16b-82c9-8c4d-2d100676c79c
```


### [WIP] zlib

WIP: https://docs.python.org/pt-br/3.14/library/compression.zstd.html#module-compression.zstd


### [WIP] annotationlib - PEP 749

https://peps.python.org/pep-0749/

WIP - Isso vai ser CHATO PRA CARAMBA!

```python
class Batata:
    def xpto(self) -> Batata:
       ...
```

## [REV] Sintaxe

### PEP 758 - Exceptions

Não precisa mais dos `()` para mais de um `except`:

```python
try:
    1/0
except ZeroDivisionError, ValueError:
    print('Deu ruim')
```

### PEP 765 - não permitir return/break/continue que saia de um bloco finally

https://peps.python.org/pep-0765/

```python
def xpto():
    try:
        ...
        raise Exception('Deu ruim!')
    except Exception:
        raise KeyboardInterrupt('Deu ruim!')
    finally:  # O que vai rolar???
       return 'OK'
```

```
<python-input-3>:8: SyntaxWarning: 'return' in a 'finally' block
```


### PEP 750 - Template strings

Vai ganhar uma live específica. Por agora, somente um exemplo:

```python
from string.templatelib import Template, Interpolation

attributes = {"src": "shrubbery.jpg", "alt": "looks nice"}
template = t"<img {attributes} />"

def html(template: Template) -> str:
    parts = ''
    for item in template:
        if isinstance(item, str):
            parts += item
        elif isinstance(item, Interpolation):
            val = item.value
            if isinstance(val, dict):
                parts += ' '.join(f'{k}="{v}"' for k, v in val.items())

    return parts

>>> html(template)
'<img src="shrubbery.jpg" alt="looks nice" />'
```


## [WIP] Interpretador

### Um novo tipo de interpretador

WIP: https://docs.python.org/pt-br/3.14/whatsnew/3.14.html#a-new-type-of-interpreter
WIP: fidgetspinner

### PEP 734 - múltiplos interpretadores na biblioteca padrão

Já tem live sobre: https://youtu.be/PaTwb2ytFUg

### PEP 779: Python com threads livres é oficialmente suportado

WIP

### PEP 744: Versões binárias para o compilador experimental just-in-time

Já tem live sobre: https://youtu.be/c8ZxdwTv8N8?t=5288
