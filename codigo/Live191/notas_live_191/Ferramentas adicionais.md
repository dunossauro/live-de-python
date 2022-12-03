# Ferramentas adicionais

Até aqui, aprendemos sobre bibliotecas, repositorios, gerenciadores, e máquinas virtuais. Com apenas isso, teoricamente teriamos tudo o que precisamos para administrar nossos projetos e os pacotes deles. Porém, existem outras ferramentas externas que foram feitas para nos ajudar ou com propositos similares às que o Python possui nativamente. Vamos ver algumas delas.

## Amigos do venv

### virtualenv

Sim, por mais confuso que pareça, **virtualenv** e **venv** são coisas diferentes. O **virtualenv** é um pacote que começou a ser desenvolvido pela PyPA antes do **venv** existir, para resolver os problemas que comentamos (e alguns outros). Depois de algum tempo, o time de desenvolvimento do Python viu que era uma ótima ideia, e decidiu adicionar um pedaço do projeto nas bibliotecas padrão do Python, e assim nasceu o **venv**.

Então, **venv** é uma parte da biblioteca **virtualenv**. Caso você decida instalar a **virtualenv**, além de funcionalidades adicionais também existem algumas vantagens:

- Ele é mais rápido
- Ciclo de lançamento separado do Python
- Extensível
- Tem uma API de código

## virtualenvwrapper

Pacote criado para facilitar a criação e a manutenção de ambientes virtuais.

## Amigos do python

### pyenv

Me permite instalar várias versões de python num ambiente (virtual ou físico).

### tox

Pacote para rodar teste em diferentes versões do python, bom para criar bibliotecas já que elas precisam funcionar em várias versões diferentes do python.

### pipx

Instala ferramentas de linha de comando em um ambiente virtual isolado, como se fosse um flatpak do python. Quando eu instalo um pacote por ela, ela cria um ambiente isolado para aquele pacote e não suja o meu ambiente global. É muito bom para instalações de pacotes que devem ser globais, como o virtualenv ou o poetry.

## O mundo científico

Na academia e meios mais científicos, algumas outras ferramentas são bem populares.

### conda

É um gerenciador de pacotes como o pip. A diferença é que ele funciona para muitas outras linguagens comuns no meio científico, e busca em um repositório próprio diferente do PyPI, o conda-forge! Também é, além de um gerenciador de pacotes, um gerenciador de ambientes.

### Anaconda

É uma distribuição do Conda. Ele pega esse gerenciador de pacotes e ambiente, e em cima dele já instala várias linguagens e pacotes científicos mais usado. Também possui uma interface gráfica muito boa

### miniconda

Uma versão minimalista do Anaconda. Ele só instala o python e o conda, e mais alguns pacotes básicos pros dois funcionarem, e aí vc vai montando seu ambiente a partir disso.

### Mamba

Parecido com o Conda, mas reescrito em C++ pra melhorar a performance.
