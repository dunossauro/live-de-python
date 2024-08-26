# Sistema de imports

Se você me perguntar qual a parte mais complicada e mal compreendida da linguagem, certamente te direi que é o sistema de imports. Por muitas vezes nos pegamos estudando diversas partes da linguagem, porém, não me recordo de nenhum caso onde alguém efetivamente me disse que estava estudando como os imports funcionavam no python. Usamos eles a todo momento, porém, quase nunca o estudamos a fundo.

Isso acaba acarretando em diversos cenários que não são necessários:

1. Colocamos `__init__.py` em todos os pacotes. Precisa?
2. `ModuleNotFoundError`: O que isso significa?
3. Casos de imports circulares
4. Adicionamos novos caminhos no `sys.path`


## Começando pelo começo

Em python nos baseamos em um conceito chamado `namespace`, que literalmente é um espaço de nomes. Dizemos que nomes em python tem escopos. Por exemplo, se quisermos chamar a função `sum`:

```python
>>> sum([1, 2, 3])
6
```

Não importamos a função sum de nenhum local, mas podemos usar ela. De onde vem o nome `sum`? A função `sum` faz parte das funções `builtins` do python. Entenda Built-in como "coisas que não precisam de imports". Os Built-in já estão no namespace global.

### Namespace global

> Namespaces e escopos já foram tema da live de python anteriormente (https://youtu.be/nWmPEgTwGMM)

Para vermos todos os nomes definidos e que podemos usar, podemos chamar a função embutida (sim outra) chamada `globals()`:

```python
>>> globals()
{
     '__name__': '__main__',
	 '__doc__': None,
	 '__package__': None,
	 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
	 '__spec__': None,
	 '__annotations__': {},
	 '__builtins__': <module 'builtins' (built-in)>
}
```

Aqui vemos diversos nomes que podem ser usados durante a execução. Como `__name__`, `__doc__` e etc...

Temos um nome especial entre eles que é de fato o `__builtins__`. Que é onde todos os nome que não precisam ser importados estão.

> Caso queira ver as [funções embutidas](https://docs.python.org/pt-br/3/library/functions.html#built-in-funcs), as [constantes embutidas](https://docs.python.org/pt-br/3/library/constants.html#built-in-consts) e as [exceções embutidas](https://docs.python.org/3/library/exceptions.html)

#### Um detalhe de implementação

Quando chamamos um nome em python, ele buscará por esse nome no escopo global. Por exemplo:

```python
# aqui.py
sum([1, 2, 3])
```

Um nome é chamado pela instrução `LOAD_NAME` do bytecode:

```bash
python -m dis aqui.py 
  0           RESUME                   0

  1           LOAD_NAME                0 (sum)  # <--- A instrução que interessa
              PUSH_NULL
              BUILD_LIST               0
              LOAD_CONST               0 ((1, 2, 3))
              LIST_EXTEND              1
              CALL                     1
              POP_TOP
              RETURN_CONST             1 (None)
```

A instrução [LOAD_NAME](https://github.com/python/cpython/blob/d25954dff5409c8926d2a4053d3e892462f8b8b5/Python/generated_cases.c.h#L4575) procura no escopo de nomes pelo nome requerido no escopo local, caso não exista no local, procura no globa, caso não existe no global, procurará em `__builtins__`. Caso não o encontre, erro de nome ou `NameError` para os mais chegados.


### A definição de novos nomes

Os novos nomes são criados com base em coisas que definimos durante o andamento do código. Por exemplo:

```python
>>> a = 1
>>> b = 2
>>> c = 3
>>> print(locals())
{
    '__name__': '__main__',
	'__doc__': None,
	'__package__': None,
	'__loader__': <class '_frozen_importlib.BuiltinImporter'>,
	'__spec__': None,
	'__annotations__': {},
	'__builtins__': <module 'builtins' (built-in)>,
	'a': 1, 'b': 2, 'c': 3  # <-- Nomes que definimos
}
```

Dessa forma, podemos chamar estes valores posteriormente, após a definição. Pois eles estão no escopo "global" de nomes.

## Módulos

Uma coisa interessante, que você pode ter notado é que durante as chamadas de `globals` e `locals`, vemos que `__builtins__` é um **módulo**:

```python
>>> print(locals())
{
    '__name__': '__main__',
	'__doc__': None,
	'__package__': None,
	'__loader__': <class '_frozen_importlib.BuiltinImporter'>,
	'__spec__': None,
	'__annotations__': {},
	'__builtins__': <module 'builtins' (built-in)> # <-- aqui
}
```

Em python, módulos são objetos especiais. Uma "unidade organizacional de código":

```python
>>> globals()['__builtins__']
<module 'builtins' (built-in)>

>>> type(globals()['__builtins__'])
<class 'module'>
```

Os módulos têm um espaço de nomes. Ou seja, um dicionário com nomes que podemos acessar. O atributo `__dict__` nos mostra os nomes definidos em um módulo:

```python
{
 # Erros
 'ArithmeticError': <class 'ArithmeticError'>,
 'TypeError': <class 'TypeError'>,
 # Constantes
 'Ellipsis': Ellipsis,
 'False': False,
 'None': None,
 'True': True,
 '_': <class 'module'>,
 # Atributos de módulo
 '__build_class__': <built-in function __build_class__>,
 '__debug__': True,
 '__import__': <built-in function __import__>,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__name__': 'builtins',
 '__package__': '',
 '__spec__': ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in'),
 # Funções builtin
 'abs': <built-in function abs>,
 'aiter': <built-in function aiter>,
 'all': <built-in function all>,
 'vars': <built-in function vars>,
 'zip': <class 'zip'>}
```

Por esse motivo, quando chamamos a função `zip`, recebemos `<class 'zip'>`. É a implementação contida em `__builtins__['zip']`. Isso vale para todos os valores builtins.


### Objeto módulo

Os objetos módulo não podem ser criados em tempo de execução, mas, todos os tipos que não podem ser criados em tempo de execução estão em `types`. Então, vamos inspecionar o tipo módulo:

```python
>>> from types import ModuleType
>>> ModuleType('módulo')
<module 'módulo'>
```

Se quisermos, podemos inspecionar o tipo módulo usando a função embutida `dir`:

```python
>>> dir(ModuleType('módulo'))
['__doc__', '__loader__', '__name__', '__package__', '__spec__']
```

Voltaremos a esses atributos em breve!

### O que o python considera um módulo?



### Na mão

```python
>>> from importlib.util import find_spec

>>> find_spec('modulo')  # (finder) busca por specs

ModuleSpec(
  name='modulo',
  loader=<_frozen_importlib_external.SourceFileLoader object at 0x717ea38c7830>, 
  origin='/home/dunossauro/Live269/modulo.py'
)

>>> from types import ModuleType
>>> mod = ModuleType(spec.name)

def _init_module_attrs(spec, module):
    module.__loader__ = spec.loader
    module.__package__ = spec.parent
    module.__file__ = spec.origin
    sys.modules[spec.name] = module
```

## Referências

### PEPs

- PEP 302: https://peps.python.org/pep-0302/
- PEP 382: https://peps.python.org/pep-0382/
- PEP 420: https://peps.python.org/pep-0420/

### Documentação
- Builtins: https://docs.python.org/3/library/builtins.html
- Glossário: https://docs.python.org/pt-br/3/glossary.html
- Sistema de importação: https://docs.python.org/pt-br/3/reference/import.html
- Módulo sys: https://docs.python.org/3/library/sys.html
- sys path: https://docs.python.org/pt-br/3/library/sys_path_init.html#sys-path-init
- importlib: https://docs.python.org/3/library/importlib.html

### Código fonte:
- LOAD_NAME: https://github.com/python/cpython/blob/d25954dff5409c8926d2a4053d3e892462f8b8b5/Python/generated_cases.c.h#L4575

### Blogs
- https://tenthousandmeters.com/blog/python-behind-the-scenes-11-how-the-python-import-system-works/

