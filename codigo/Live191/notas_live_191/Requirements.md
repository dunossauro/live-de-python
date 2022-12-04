# Requirements

## O que é

O Requirements é uma forma de reproduzirmos ambientes.

Imagine que eu esteja trabalhando em um projeto, com um ambiente, instalando algumas bibliotecas. Depois, uma pessoa amiga minha resolve que quer me ajudar com esse projeto, então eu compartilho o código fonte. Essa pessoa então cria seu próprio ambiente, e instala uma a uma as dependencias do projeto. Porém, nesse meio tempo uma das dependencias foi atualizada pra uma nova versão. Quando a pessoa que quer contribuir for instalar essa dependencia, estaremos com versões diferentes dela! Isso pode causar bugs e problemas. Fora que instalar as dependencias uma a uma manualmente é um saco.

Mas também não faz sentido passar um venv pra outra pessoa. Pois o venv é criado pelo pip e é diferente dependendo do sistema operacional, da shell, de várias coisas.

Pra resolver esse problema, surgiu o **requirements.txt**. Nele, vão ser descrito todas as dependencias de um projeto, além da especificação da versão de cada uma delas. Com isso, pra eu conseguir trabalhar em um projeto com outras pessoas, posso apenas passar o código fonte, e o arquivo **requirements.txt**, que posso facilmente transferir.

Ele tem essa cara:

```text
# Pacotes que quero instalar
pandas
matplotlib
pytest

# Pacotes com versoes específicas
black == 0.6.1  # Igual a 0.6.1
django >= 4.1.1 # Maior que 4.1.1
flask != 3.5    # Diferente de 3.5
selenium ~= 1.1 # Maior ou igual a 1.1, mas menor que 2
```

Se não especificarmos versoes, o pip sempre baixa a última versão disponível no PyPI. Da pra fazer mto mais coisa nesse arquivo, para mais informações ler a [documentação](https://pip.pypa.io/en/stable/reference/requirements-file-format/?highlight=requirements).

Então, quando uma pessoa clonar o nosso projeto do github, ou descompactar, ela agora pode instalar facilmente as dependencias graças ao **requirements.txt**. Basta criar e ativar a venv, e dar o comando `pip install -r requirements`

Podemos criar esse arquivo com o pip, ao invés de fazer ele manualmente, com o comando `pip freeze`, que nos mostra todos os pacotes no ambiente e as versoes dele. Então depois disso basta colar isso no arquivo, com o comando `pip freeze > requirements.txt`. Agora temos um arquivo de **requirements**! Yay! Mas isso tem probleminhas: ela vai listar **TODAS** as bibliotecas, até as instaladas pois a biblioteca que eu queria depende delas. E todas as bibliotecas estão fixas com `==` nas suas versões que estão instaladas na minha máquina (`pandas==1.10.3`, por exemplo). Então eu talvez tenha que fazer algumas intervenções manuais nesse arquivo.

## Outros arquivos

Na maioria das vezes, dentro de um projeto nos utilizamos de pacotes durante o desenvolvimento que não precisam estar no ambiente de produção. Alguns exemplos são formatadores (`black`), pacotes de teste(`pytest`),  debuggers (`ipdb`), etc. Então, separamos elas em outro arquivo, o **requirements_dev.txt**. É importante adicionar no início desse arquivo a linha `-r requirements.txt`, e depois adicionar as bibliotecas de desenvolvimento. Assim, quem for instalar as bibliotecas de desenvolvimento para trabalhar junto com você no projeto pode executar apenas o comando `pip install -r requirements_dev.txt`. Você pode modularizar ainda mais isso, pode viajar aí e ir fazendo varios arquivos chamando um ao outro.

Outro arquivo importante é o **constraints.txt**. Esse arquivo serve para restringirmos quais versões de bibliotecas **NÃO** quero que sejam instaladas. Por questões de segurança, burocracia empresarial de autorização, bugs específicos de uma versão da biblioteca, etc. Ele tem o mesmo formato do requirements. Para baixar levando em conta essas restrições, usar o comando: `pip install -r requirements_dev.txt -c constraints.txt`

## Bibliotecas auxiliares

Não vou entrar muito em detalhes aqui, mas duas bibliotecas legais para se olhar são a `pip-autoremove`, que serve pra remover um pacote *e suas dependencias*, ao inves de apenas o pacote especificado. E também a `pipdeptree`, que lista as bibliotecas e suas dependencias em um formato de arvore.
