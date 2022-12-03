# Ambientes Virtuais

## O que são?

**Ambientes Virtuais** são ambientes isolados do Python. Ele vai criar um ambiente local do Python dentro de uma pasta específica de um projeto, isolada do meu ambiente global da minha máquina.

Elas servem para eu poder instalar as minhas bibliotecas localmente para cada projeto. Então quando crio um **ambiente virtual** num projeto, nesse ambiente vai existir uma pasta de bibliotecas. E quando instalo uma biblioteca (`pandas`, por exemplo), ela não vai estar disponível globalmente apenas localmente, pois ela vai ser instalada nessa pasta local. Isso é importante, pois para cada projeto posso isolar minhas bibliotecas e dependencias. Isso resolve nossos dois problemas apresentados:

No primeiro caso, posso especificar pro pip instalar a versão 1.4 do Pandas no **ambiente virtual** do projeto 1, e a versão 2.0 do Pandas no **ambiente virtual** do projeto 2.

Já no segundo caso, como só vou baixar os pacotes necessários para aquele projeto específico, a chance de dois pacotes terem conflito de dependencias é bem menor.

## Como criar?

O método padrão é utilizar o pacote **venv**, que já vem incluso no python. Vou usar os comando baseados no Linux, mas os comandos são ligeiramente diferentes para cada sistema. Consulte a [documentação](https://docs.python.org/3/library/venv.html) para instruções detalhadas.

Primeiro, para cirar o ambiente basta usar o comando:

```python
python -m venv <nomedapasta>
```

E ele vai criar a pasta do ambiente virtual com o nome dado. No entando, o mais comum é utilizarmos o próprio nome `venv`, então o comando ficaria:

```python
python -m venv venv
```

## O que foi criado?

Dentro da pasta `venv`, existem alguns arquivos e pastas, vamos entender cada um deles. De novo, aqui é específico para cada sistema, consulte a [documentação](https://docs.python.org/3/library/venv.html) para mais detalhes

O arquivo `pyenv.cfg` possui três configurações:

```python
# Onde o python global está instalado
home = /usr/bin
# Se devo incluir a pasta de bibliotecas globais
include-system-site-packages = false
# A versão do python
version = 3.10.6
```

A pasta `/bin` possui os binários a serem executados.

A pasta `/include` possui alguns arquivos de instruções pro sistema.

A pasta `/lib` é a minha nova pasta de bibliotecas, onde elas vão ser instaladas localmente. Ela já vem populada com o `pip`, pois precisamos dessa biblioteca para instalar novos pacotes. Também vem com `setuptools`, um outro pacote para lidar com pacotes, também necessário para o funcionamento da venv (afinal, ela serve pra isolar pacotes ne :D).

A pasta `/lib64` é um link simbólico para a pasta `/lib`

## Ativando e desativando o venv

Depois de criado o ambiente virtual (venv), precisamos ativar ele. Isso faz com que a nossa linha de comando opere internamente ali naquele terminal, e o caminho de referencia pros pacotes passa a ser o venv ao invés do global do Python. Para ativa uma venv no Linux, usando bash ou zsh, o comando é: `source venv/bin/activate` (muda para cada shell e cada sistema. De novo, leia as docs).

E pronto! Agora, estamos em um ambiente com nossas próprias bibliotecas locais, que está isolado do sistema global!
Se eu quiser voltar para meu ambiente global, basta eu dar o comando `deactivate`!

## Venv em ação

Vamos para um exemplo prático, para solidificar o nosso conhecimento. Eu acabei de instalar o python na minha máquina, e quero fazer um projeto que vai puxar coisas da web, e pra isso vou usar o pacote `httpx`.

Como acabamos de aprender, é uma boa prática isolar os pacotes de cada um dos meus projetos. Então dentro da pasta do meu projeto `puxar_coisas_internet`, vou criar a venv, e já ativar ela!

`python -m venv venv`
`source venv/bin/activate`

Agora, vou instalar o pacote.

`pip install httpx`

O pip vai até o PyPI, baixa o pacote, e instala ele dentro da minha venv.

E por fim, vou fazer o meu scritp!

```python
from httpx import get
print(get(http://ddg.gg))
```

Esse script bem simples só imprime o resultado de um método http `get` no site do DuckDuckGo. Se eu executar esse script com `python script.py`, vou receber uma mensagem mais ou menos assim: `<Response [301 Moved Permanentely]`. Não precisa se preocupar com entender isso agora, é só pra vermos que conseguimos instalar o pacote `httpx`, e que ele já está funcionando, pois nosso script executou normalmente!

Mas e se eu desativar o meu venv com `deactivate` e depois tentar rodar o meu programinha, com `python script.py`? Ele vai me dar erro! Mais específicamente, esse erro:

`ModuleNotFoundError: No module named 'httpx'`

O que é esse erro? Ele está me dizendo que ele não conseguiu achar algum módulo... O httpx! Eu instalei ele no ambiente virtual, mas não no ambiente global! Então, quando eu desativo o venv, ele volta a puxar os pacotes do ambiente global, onde o pacote httpx não existe, pois ele não foi instalado. Bacana, não?
