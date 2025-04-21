## recap

- namespaces
  - Local
  - Global

- imports
 - Como são encontrados
   - Loaders
   - Finders


## O que são módulos

Como tudo, ou quase tudo, módulos também são objetos. Você pode criar um módulo em runtime usando `type.ModuleType`:

```python
>>> from type import ModuleType
>>> modulo = ModuleType('Módulo')
>>> type(modulo)
<class 'Módulo'>


>>> modulo.__spec__
# None
```

---

## O básico, um arquivo importado

```python
>>> import modulo_00
>>> modulo_00.__spec__
ModuleSpec(
    name='modulo_00', # nome do arquivo
	# Estratégia de carregamento do arquivo
	loader=<_frozen_importlib_external.SourceFileLoader object at 0x7b441ca1cd70>, 
	# O lugar onde o arquivo está
	origin='/home/dunossauro/live_modulos_e_pacotes/modulo_00.py'
)
>> dir(modulo)
```

---

```python
# Todos os nomes do namespace do módulo
>>> dir(modulo_00)
[
    '__builtins__',
	'__cached__',
	'__doc__',    # Docstring do módulo
	'__file__',   # Local do arquivo
	'__loader__',
	'__name__',   # modulo_00
	'__package__',
	'__spec__',
	'soma'        # Nome que definimos explicitamente
]
```

---

## Dunders de módulos

Alguns nomes *especiais* podem ser usados em módulos, como:

- `__author__`: Nome que diz de quem é a autoria do módulo
- `__version__`: Usado para versionamento dinâmico
- `__all__`: O que será importado via *star* (`from modulo import *`)

---

Especificação de autoria do módulo/pacote

```python
# modulo.py
__author__ = 'Fausto, o Mago!'
```

---

O `__version__` é usado mais no sentido de pacotes, ele pode determinar a versão de um pacote dinamicamente:

```python
# pacote/__init__.py
__version__ = '0.4.7b3'
```

---

> AQUI

Os backends de build podem usar esse valor para determinar a versão do empacotamento do pacote:

```toml
# pyproject.toml
[project]
name = 'pacote'
dynamic = ['version']
# pacote.__init__.__version__
```

> TODO: Isso deveria estar aqui? Pode ser citado e levado para a parte de **pacotes**
>       Pensar se quero mostrar um backend de build,
>       Se sim, instalar o `pypa-build`
>       `python -m build modulo`

---

## `__all__`


> TODO: Fazer um módulo com N nomes, mostrar o import from e mostrar o import *

---

