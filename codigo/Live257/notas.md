# Empacotamento Python
## Antes dos padrões (Antes de 2000)

Python teve sua primeira release compartilhada em 1991 (0.9.0), nesse ponto, se você quisesse compartilhar um código python com outras pessoas por meio dos próprios arquivos mesmo. O PyPI ainda não existia.

Espera....

https://web.archive.org/web/20080406143246/http://py.vaults.ca/~x/parnassus/

## Distutils - 2000

Em 1998 foi criado o distutils-SIG [Special Interest Groups] para discutir um formato padrão para distribuição de código python. Do grupo de pessoas interessadas, surgiu o `distutils`. Ferramenta **padrão** de empacotamento/instalação de pacotes do python. Foi incluida na versão 1.6 na biblioteca padrão e presente até a versão `3.11`.

### Empacotando

A ideia do empacotamento nesse ponto é bastante simples. Foi definido que um arquivo `setup.py` seria criado na raiz do projeto e sua chamada seria um CLI para o build e distribuição do pacote:

```python
# setup.py
from distutils.core import setup

setup(
    name='package',
    version='0.0.1',
	# O pacote deve ter um `__init__.py` para ser reconhecido como um módulo.
    packages=['app'],
)
```

O arquivo de setup podia fazer o build do pacote de duas formas. No formato binário (`bdist`) e no formato de código fonte empacotado (`stdist`).

Você poderia executar as chamadas da seguinte forma:

```bash
python setup.py sdist  # para distribuição do fonte
python setup.py bdist  # para distribuição binária
```

Resultando em dois arquivos:

```
.
├── app
│  ├── __init__.py
│  └── __main__.py
├── dist
│  ├── package-0.0.1.linux-x86_64.tar.gz  # bdist
│  └── package-0.0.1.tar.gz               # sdist
└── setup.py
```

O binário é específico por plataforma, enquanto o sdist é basicamente um zip do diretório do pacote.

### Instalando

Para instalar o pacote, seguimos a mesma lógica:

```bash
python setup.py install
```

Dessa forma temos o pacote instalado em nosso sistema.

## A loja de queijos [PyPI] - 2002/2003

Embora fosse muito interessante criar pacotes, não existia um lugar **padrão** para sabermos "quais pacotes existem". Nisso foi criada o `Cheese Shop`. Um index oficial de pacotes, descrito na [PEP-031](https://peps.python.org/pep-0301/).

Em 2023 estava no ar o PyPI, o Python Package Index. Até esse momento ele era somente um index, os pacotes não estavam no PyPI. Isso explica o nome, que parece estranho nos dias de hoje, já que não é mais um index e sim um repositório de pacotes.

> Os pacotes começaram a ser armazenados no pypi em 2005

## Setuptools - 2004

Embora tivéssemos uma forma padrão de fazer build e instalação de pacotes com o [distutils](#distutils-2000). O distuils carecia de uma forma simples de especificar dependências. Por exemplo, se eu criasse uma aplicação e ela dependesse de X pacotes, eu teria que fazer vendoring dos pacotes e instalá-los manualmente. O que tornava as cosias complicadas de mais.

O setuptools se aproveita da estrutura criada pelo distutils, inclusive é buildado por ele, e expande as funcionalidades do arquivo `setup.py`

```python
# setup.py
from setuptools import setup

setup(
    name='package',
    version='0.0.1',
    packages=['app'],
	# ISSO!
    install_requires=['rich', 'rich-pixels', 'pillow']
)
```

### Eggs

No processo de build, foi introduzido um novo formato binário de distribuição, o [`egg`](http://peak.telecommunity.com/DevCenter/PythonEggs). A ideia dos eggs é armazenar os metadados e as dependências dais quais o seu pacote depende. Fazendo assim uma rede de pacotes. Por exemplo, `A` usa `B` e `B` usa `C`. Nos metadados era possível saber quais pacotes e em quais versões as dependências deveriam estar instaladas no ambiente.

### Easy install

Junto com o `setuptools` uma ferramenta de CLI incorporada. Chamada de `easy_install`. Ele era capaz de percorrer os arquivos `.egg` atrás de seus metadados e fazer o download e instalação das dependências no seu ambiente.

Da seguinte forma:

```bash
# procurando os pacotes no index do PyPI
easy_install pacote
# faz o download e o build do sdist
easy_install http://example.com/path/to/MyPackage-1.2.3.tgz
# instala um .egg local
easy_install /my_downloads/OtherPackage-3.2.1-py2.3.egg
# instala o pacote local com setuptools (baixa as dependências e faz o build de cada uma)
easy_install .
```

## Virtualenv - 2007

Bom, só gostaria de pontuar quando ele foi criado mesmo. Nenhuma informação relevante aqui...

### -m venv vs virtualenv

Embora o virtualenv tenha sido criado em 2007, a sua inclusão na biblioteca padrão só aconteceu na versão 3.3 do python em 2012. O `virtualenv` é a implementação completa de cheia de ferramentas, o módulo `venv` da biblioteca padrão é somente um pedaço do código do virtualnev mantido pelo PyPA.

## Pip - 2008

O desenvolvimento do pip (pip install package) tinha o objetivo de corrigir alguns problemas gerados pelo [easy_install](#easy-install). Como a desinstalação dos pacotes, que ainda não eram possíveis, listagem dos pacotes instalados e a substituição de dependências, como alterar as versões dos pacotes instalados. O pip foi incluído na biblioteca padrão na versão 3.4 (2014).

### requirements.txt

A introdução do pip é feita em uma etapa do ciclo do python onde os builds eram facilitados pelo setuptools, pacotes estavam disponíveis no PyPI e também isolados em ambientes virtuais. Com uma gama de elementos, suge uma nova necessidade a de construir ambientes e aplicações que dependam de muitos pacotes externos. Assim surge o `requiremets.txt`.

Um arquivo formado por uma lista de dependências **concretas** para que o ambiente local possa ser reproduzido em outros lugares.

```text
rich==13.7.0
rich-pixels==3.0.0
typer==0.9.0
inquirerpy==0.3.4
```

> Uma especificação para a "pinagem" de versão foi introduzida na PEP-440

### Dependências concretas vs abstratas

Agora uma pergunta pode ter ficado no ar. No `setup.py` já especificávamos as dependências usando o campo `install_requires`, devemos fazer isso novamente no `requirements.txt`?

O setup é responsável por fazer builds de coisas reutilizáveis no sistema. Como bibliotecas ou frameworks. Neste caso, um pacote pode depender de outros pacotes.

Nesse cenário, não é possível pinar um pacote. Imagina que lib A depende de B na versão exata 1.1.1, e C depende de B na versão exata 1.1.0. Isso se torna um problema. Nesse caso, o setup deve conter dependências não travadas, ou seja, abstratas. Enquanto o requirement, que monta seu ambiente, deve as referências concretas, para que ele possa ser reproduzido.

Neste caso, tanto requirements, quanto setup, tem papeis diferentes dentro do seu ambiente. É capaz que você nunca tenha desenvolvido uma biblioteca em anos programando python e sua referência seja apenas o `requirements.txt`.

## [NF] Ministry of installation [PyPA] - 2011



## PEP-427 (wheel) - 2012 (post 2013)

Com os erros aprendidos com o formato `eggs`, essa PEP visa a padronização de um formato de build para distribuição (bdist) chamado "wheel".

O arquivo wheel nada mais é que um arquivo zip formatado com a extensão `.whl`. O nome do compactado final deve ter essa forma:

`{distribution}-{version}(-{build tag})?-{python tag}-{abi tag}-{platform tag}.whl`

Onde os mais importantes são:

- distribution: o nome do pacote
- version: a versão do pacote
- python tag: Versão do python em que o pacote deve ser usado
- platform tag: tag para um sistema operacional específico. Para todos é `any`

> As tags abi são um assunto a parte. Na [documentação do PyPA existe bastante insumo para isso](https://packaging.python.org/en/latest/specifications/platform-compatibility-tags/)

Existem DIVERSOS recursos sobre os que não falarei aqui, mas é importante saber pelo menos sobre a nomemclatura. Para mais informações sobre os arquivos contidos e a forma do empacotamento, consulte a PEP-427.


## PEP-518 (build-system e tools)- 2016

Inicia a discussão sobre a criação de uma especificação mínima para sistemas de build.

A ideia principal dessa PEP é mostrar como um pacote deve especificar suas próprias dependências de build. O que é necessário que o ambiente tenha, para que o build possa ser feito.

Nisso, fica especificado que um arquivo chamado `pyproject.toml` será utilizado para esse fim. O arquivo no `toml` foi escolhido por ser bom de ler/escrever por humanos (diferente do JSON), flexível o suficiente (diferente do configparser), é originado por um padrão (também diferente do configparser) e não é complicado (como YAML).

### Um pouco sobre o toml

TOML implementa diversos tipos de dados, sendo o primordial para o `pyproject` as tables. Que são equivalentes a dicionários em python:

```toml
# Comentário !
[table]
chave_0 = true  # booleano
chave_1 = 'valor 1'  # string
chave_2 = ['valor 1 no array', 'valor 2 no array']  # array de strings
chave_3 = 1  # inteiro
chave_4 = { nome = 'pyproject', extensao = '.toml'}  # Cria uma subtabela em uma linha

[table.subtable]  # Cria uma subtabela
chave_0 = 1.0  # float

[table.subtable.subsubtable]
chave_0 = 2024-01-01
```

Seria o equivalente ao dicionário python:

```python
{'table': {'chave_0': True,
           'chave_1': 'valor 1',
           'chave_2': ['valor 1 no array', 'valor 2 no array'],
           'chave_3': 1,
           'chave_4': {'extensao': '.toml', 'nome': 'pyproject'},
           'subtable': {'chave_0': 1.0,
                        'subsubtable': {'chave_0': datetime.date(2024, 1, 1)}}}}
```

### A especificação

A especificação se baseia em duas tables, uma para o sistema de build (`build-system`) e outra para ferramentas em geral (`tool`).

#### A tabela de build-system

A tabela referente ao sistema de builds tem uma única chave chamada `requires`[^1], que será um array de todas as ferramentas que devem estar presentes no sistema no momento do build.

```toml
[build-system]
requires = ["setuptools", "wheel"]  # Suporta a PEP-508, ex: setuptools~=64.0
```

Desta forma, caso essas ferramentas não existam no ambiente, alguma ferramenta pode instalar (por padrão, o pip)


#### A tabela de tools

Diferente da tabela de `build-system` que tem objetivos relacionados ao propósito da PEP, a tabela `tool` pode ser usada por qualquer ferramenta que relacionada ao seu projeto python, não somente a ferramentas de build.

A recomendação de uso é que cada ferramenta crie sua própria subtabela de tools segunda por `.ferramenta`.

Alguns exemplos de ferramenta não relacionadas a build que usam a tabela de tool:

- Pytest: Biblioteca de testes
- Ruff: Linter e formatador
- towncrier: Gerador de changelogs (merece uma live?)
- mypy: Checador de tipos

Exemplo de uso:

```toml
[tool.ruff]
line-length = 79
exclude = ['.venv', 'migrations']

[tool.pytest.ini_options]
pythonpath = "."
```

Da mesma forma, ferramentas relacionadas a build também precisam ser configuradas, como:

- hatch
- setuptools
- poetry
- flit
- pdb

Logo, elas também podem usar a tabela:

```toml
[tool.hatch.envs.test]
dependencies = [
  "pytest"
]

[tool.setuptools.package-data]
"_pytest" = ["py.typed"]
"pytest" = ["py.typed"]
```

## PEP-517 (especificação do build-system) - 2015 (post 2017)

Esta PEP tem o objetivo de definir um formato de build independente das ferramentas já existentes. Como `buildutils` e `setuptools`, definidas pelo `distutils-sig`. Se você quiser usar outra coisa, isso deve ser fácil de fazer e também deve ser fácil para novas ferramentas serem criadas.

Desde a PEP-427 (2012) o formato padrão dos binários é o `wheel`. Isso faz com que todos os pacotes distribuídos sejam únicos.

A PEP divide a o sistema de builds em duas partes, o backend e o frontend.

```mermaid
Graph TD
Build --> Backend
Build --> Frontend
```

### Backend

O backend é responsável por compilar um pacote para distribuição em código (sdist) e no formato binário (bdist).

Para fazer isso as ferramentas de backend devem implementar algumas chamadas (hooks / funções) obrigatórias:

- `build_wheel`: Função que cria o pacote binário especificado na PEP-427
- `build_sdist`: Função que faz a compactação da biblioteca em um `tar`

> Existem outros opcionais, mas acredito que a leitura da PEP-517 pode aprofundar mais. A PEP-660 (2021) expande novos hooks opcionais para que os wheels sejam editáveis.

O sistema de builds deve implementar um módulo com os hooks, esse hooks devem ser implementados na chave `build-backend`. Algo como:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

> Exemplo de backend (https://github.com/pypa/hatch/blob/master/backend/src/hatchling/build.py)

Por exemplo:

```python
# hatchling/build.py

def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    ...
	
def build_sdist(sdist_directory, config_settings=None):
    ...
```

Assim, o frontend pode chamar o módulo `build-backend`, que por consequência, chama os hooks.

#### Buildando os backends com backends

Um problema comum ao criar um backend é que para que seu build seja feito, ele precisa conseguir chamar a si mesmo. Para isso foi criada uma nova chave na tabela `backend-path`. Para especificar onde o módulo que contém os hooks estão:

```toml
[build-system]
requires = []
build-backend = "backend.back"
backend-path = ["."]
```

### Frontend

O frontend é responsável por configurar o ambiente de build do pacote. Não é exigido nenhum ambiente em específico, a recomendação é que se use o `virtualenv`. Aí ideia é que o hooks sejam chamados em subprocessos (`subprocess`) e que os pacotes sejam pelo backend.

```mermaid
frontend --> subprocesso
subprocesso --> backend
```

Várias ferramentas podem agir como frontend e o objetivo é que sejam agnósticas nas chamadas. Pois os backends devem seguir a especificação.

Duas ferramentas em particular são importantes nesse contexto. O [`build`](https://github.com/pypa/build), criado pelo PyPA para ser uma ferramenta genérica para o `pyproject.toml` e o `pip`.

#### build
A ideia do build é simplesmente conseguir gerar a distribuição de forma independente do backend. Podendo ser usado com qualquer ferramenta.

```bash
pip install build
python -m build
```

Com um simples comando, qualquer pacote pode ser buildado.

#### pip

O `pip` por outro lado faz a chamada para o backend, que instala os pacotes e após o build pronto, instala o resultado do build.

```bash
pip install .
```

## PEP-621 (metadados para build-system) - 2020

Embora um sistema mínimo de build tenha sido criado e bem utilizado por ferramentas. Alguns pontos do modelo "agnóstico" ainda não estavam sendo levado em consideração. Os metadados do projeto.

Os backends não tinham um padrão definido para o `nome` do pacote, sua `versão`, seus `scripts`, duas `dependencias`, etc. O que tornava a migração entre backends um grande trabalho e diminuí a facilidade "pregada" pela PEP-518.

Com isso a PEP especifica uma nova tabela opcional[^2] no `pyproject.tom` chamada `project`. Que agrupa todos os metadados sem depender de uma tabela `[tool.backend]`.

A especificação diz que os valores atrelados as chaves podem ser de dois tipos:

- Estaticos: Metadados especificados no próprio arquivos e que não podem ser alterados
- Dinâmicos: Metadados marcados em um array com a chave `dynamic`, que serão fornecidos pelo build-system

### Chaves obrigatórias

- name: Nome do pacote [*estática]
- version: Versão do pacote

Fornecendo uma tabela como:

```toml
[project]
name = 'package'
version = '0.1.0'
```

ou em sua versão dinâmica:

```toml
[project]
name = 'package'
dynamic = ['version']
```

O exemplo de definição dinâmica pode ser visto no hatch como:

```toml
[tool.hatch.version]
path = "src/hatch_demo/__about__.py"  # arquivo que contem a variável __version__ = "0.1.0"
```

### Chaves opcionais

Entre as chaves opcionais estão uma grande variedade de chaves, como:

- description: String de descrição do pacote
- reame: String com o caminho do arquivo `'readme.md'`
- license: Subtabela indicando o arquivo `{file = 'LICENSE.txt'}`
- authors: Array de subtabelas inline `[{name = 'duduzinho', email = 'test@mail'}]`
- manteiners: Array de subtabelas inline `[{name = 'duduzinho', email = 'test@mail'}]`

> As definições atualizadas de metadados podem ser encontradas aqui: https://packaging.python.org/en/latest/specifications/pyproject-toml/#declaring-project-metadata-the-project-table

Nas chaves opcionais eu gostaria de destacar o campo que especifica as dependências do projeto. Um array listando todos os pacotes que nosso pacote depende (uma espécie de requirements):

```toml
[project]
dependencies = ['httpx', 'trio', 'anyio']
```

Desta forma, quando pedirmos para o frontend fazer o build do nosso pacote, o backend instalará as dependências listadas na chave `dependencies`.

Por exemplo, podemos instalar as dependências do projeto usando `pip`:

```bash
pip install .
```

Isso instalará as dependências.

### Subtabelas

Dentro da tabela `project` você pode definir diversas outra tabelas, vou destacar as que considero mais interessantes agora:

- `optional-dependencies`: Uma tabela que cria grupos de dependências. Como dependências de testes, documentação e etc...
- `scripts`: Executáveis do pacote.

A subtabela de dependências opcionais:

```toml
[project]
name = 'package'
version = '0.1.0'
dependencies = ['httpx', 'trio', 'anyio']

[project.optional-dependencies]
dev = ['ruff', 'mypy']
test = ['pytest', 'pytest-cov']
doc = ['mkdocs']
```

Podendo ser instaladas assim:

```bash
pip install .[dev]
pip install .[test]
pip install .[doc]
```

A subtabela de `scripts` também é interessante para criar CLIs ou entradas para GUIs diretamente do pacote:

```toml
[project.gui-scripts]
spam-gui = "spam.main:gui"

[project.scripts]
spam-cli = "spam.main:cli"
```

## [WIP] Futuro?

Embora tenhamos andado um bastante pelo sistema de builds e instalação de pacotes, ainda existem pontos em aberto.

1. Instalação sem build pelo pip:
2. Dependências determinísticas sem requirements.txt:

---

[^1]: Isso na PEP-518, na PEP-517 existe a chave `build-backend`

[^2]: Por esse motivo ferramentas como Poetry não aderiram ([ainda](https://github.com/python-poetry/roadmap/issues/3)), dada a não obrigatoriedade. E ferramentas como flit mantém esse campo como opicional, podendo usar tanto [project], quanto [tool.flit].
