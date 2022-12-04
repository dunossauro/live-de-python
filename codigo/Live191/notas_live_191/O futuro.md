# O futuro

Tudo isso que a gente falou vai ser atualizado e mudado.

**O QUE?** Sim, a gente está em processo de mudar como a gente faz tudo isso que acabamos de aprender.

"Bom pra que diabos eu li sobre todas essas coisas então?", você pode estar se perguntando. Pelo simples motivo que conhecer um problema e o que motivou a solução é importante na hora de entender uma ferramenta. Conhecer essas dificuldades, processos e soluções é importante para entender o nosso futuro: o **toml**

## Tom's Obvious Minimal Language

O arquivo **pyproject.toml** é o formato para o qual estamos migrando no momento. Ele já foi aprovado, e já tem um parser dele no python 3.11, mas ainda não está completamente estabelecido, ainda tem um caminho a ser trilhado.

Hoje, o `requirements.txt`,  `requirements_dev.txt`, `setup.py` vão poder ser todos substituidos por um unico arquivo `pyproject.toml`.
Ele tem um formato muito interessante, e vale a pena dar uma lida na [documentação](https://toml.io/en/) pra entender como ele funciona.

## O futuro, hoje

Existem alguns pacotes que hoje já lidam com o `pyproject.toml`, e com a forma como o python está buscando funcionar no futuro.

Um deles é o `poetry`!

### Poetry

É um pacote que busca ser o futuro do python, hoje. Ele consegue, sozinho, gerenciar:

- Ambientes virtuais (venv)
- Instalação de bibliotecas (pip)
- Versões de bibliotecas (requirements.txt)
- Lidar com os metadados de pacotes (setup.py)
- Empacotamento (setup.py + setup.cfg)

Uma alternativa, menos famosa mas bem similar ao Poetry, é o pacote `Flit`

## O futuro do futuro

Hoje existe uma discussão de se acabar com as virtualenvs! Sim, nas **PEPs** (*Python Enhance Proposal* ou *Propostas de Melhoria do Python*, em tradução livre) está sendo discutido a possibilidade de extinguir as venvs. Mais especificamente essa é a [PEP 582](https://peps.python.org/pep-0582/).

Se você estiver muito interessado nesse futuro do futuro, você pode experimentar ele usando o [PDM](https://pdm.fming.dev/latest/), que é um gerenciador de pacotes que tenta simular esse futuro.
