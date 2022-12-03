# Bibliotecas

## O que são?

Bibliotecas são códigos feitos por outras pessoas. Elas podem ser instalados no meu computador para adicionar funcionalidades ao Python. Um exemplo é a biblioteca Pandas, que adiciona ao Python diversas formas de lidar com dados para os manipular e analisar esses dados.

## Como são instaladas as Bibliotecas?

### Repositorios

Para instalar uma biblioteca, ela primeiro precisa ser criada, e publicada em algum lugar. Esse lugar é chamado de **repositório**, ou **index**, no inglês. O mais famoso é o *PyPI*, que é uma sigla para *Python Package Index* (*Repositório de Pacotes Python*, em tradução livre).

Nos repositórios, os desenvolvedores podem disponibilizar seus códigod no formato de bibliotecas, onde outros desenvolvedores vão poder baixar e utilizar esse código. Assim, evitamos o retrabalho, e vamos sempre avançando e construindo coisas novas e melhores em cima de coisas boas já feitas anteriormente.

### Como instalar uma biblioteca

Usando um **gerenciador de pacotes**. O mais famoso, é o *pip*, que é uma sigla para *Python Install Package*. Ele é um pacote que chamamos de *built-in*, pacotes que vêm imbutidos no Python. O que os **gerenciadores de pacotes** fazem é abstrair para usuários o processo de instalação de pacotes. Ele vai até o **repositório** e baixa a biblioteca, e instala ela pra você na sua máquina.

O pip é a forma recomendada de se instalar pacotes no Python, segundo a *PyPA*, sigla para *Python Packaging Authority* (*Autoridade de Gerenciamento de Pacotes do Python*, em tradução livre). Existem outros gerenciadores de pacote, mas vamos falar deles depois.

### Onde são instaladas as bibliotecas?

Show, já sei que eu preciso ir até um **repositório** e baixar a minha biblioteca, e que existe **gerenciadores de pacotes** para abstrair esse processo pra mim. Mas, aonde fica a biblioteca no meu computador para o Python conseguir utilizar ela? Numa pasta **global** de bibliotecas. Chamamos ela de **global** pois todos os seus projetos vão ter acesso às bibliotecas instaladas aqui. E isso pode nos criar problemas. Para entender melhor eles, precisamos entender o que é o **path**

### Entendendo o Path

O **Path** (caminho, em tradução literal pro português) é uma lista de caminhos onde o Python vai procurar uma biblioteca quando usamos o comando `import`. Podemos checar ela importando o pacote `sys`, como no exemplo:

```python
import sys
print(sys.path)
""" Vai ser algo parecido com essa lista:
['',
 '/usr/lib64/python310.zip',
 '/usr/lib64/python3.10',
 '/usr/lib64/python3.10/lib-dynload',
 '/home/<username>/.local/lib/python3.10/site-packages',
 '/usr/lib64/python3.10/site-packages',
 '/usr/lib/python3.10/site-packages']
"""
```

Vamos analisar esses caminhos, pois o Python vai procurar em ordem de cima pra baixo neles quando usamos o `import`.

O primeiro caminho (vazio) quer dizer que ele vai procurar uma pasta com o nome passado na pasta que o arquivo python está sendo executado.

Os dois caminhos seguintes são as pastas do próprio Python, ou seja, ele está procurando pelas bibliotecas padrões da liguagem que já vem instaladas junto com ela.

O caminho com lib-dynload é relativo ao Python dev, que serve pra compilar o Python na máquina.

Só então ele vai procurar pelo pacote na pasta `home` do meu usuario, onde estão sendo instalados se eu rodar o comando `pip install pandas`.

Por fim, ele vai procurar nos caminhos do python instalado na minha máquina independentes de usuário, ou seja, onde o pip instalaria o pacote se eu rodasse o comando logado como usuário `root` no sistema.

Essa lista vai ser um pouco diferente para cada pessoa e máquina, mas em resumo: O python busca o pacote na pasta que o script está sendo executado, depois procura nas bibliotecas built-in, depois nas bibliotecas globais do usuário, e por fim nas bibliotecas globais da máquina (independente de usuários). Chamamos essas duas últimas de *globais* pois todos os arquivos Python no meu sistema vão ter acesso à essas bibliotecas. Diferente de um pacote local, desenvolvido na própria pasta do projeto, onde só os arquivos daquele projeto vão ter acesso ao pacote.

### Recapitulando

Uma biblioteca é publicada num **repositório**, onde pode ser baixada. A forma mais comum de se baixar de um **repositório** é usando um **gerenciador de pacotes** que baixa esse pacote e instala na minha máquina em uma das pastas **globais** do meu computador, descritas no **path**. Por fim, quando damos o comando `import` num arquivo Python, ele procura pelo pacote nos diretórios descritos no **path**, em ordem. E assim finalmente podemos utilizar esse pacote.

Era isso que precisavamos aprender sobre as bibliotecas em si. Ok, mas por que isso é importante? O fato do gerenciador de pacotes por padrão instalar um pacote  pode nos causar problemas. Nos próximos notebooks vamos aprender sobre esses problemas.
