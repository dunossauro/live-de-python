from pathlib import Path

base = Path('namespace_demo')

estrutura = {
    'pkg1/meupacote/mod1.py': """\
def diga_ola():
    print("Olá do mod1!")
""",
    'pkg1/pyproject.toml': """\
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "meupacote-mod1"
version = "0.1"
description = "Parte 1 do namespace meupacote"

[tool.setuptools.packages.find]
where = ["."]
""",
    'pkg2/meupacote/mod2.py': """\
def diga_ola():
    print("Olá do mod2!")
""",
    'pkg2/pyproject.toml': """\
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "meupacote-mod2"
version = "0.1"
description = "Parte 2 do namespace meupacote"

[tool.setuptools.packages.find]
where = ["."]
""",
    'teste.py': """\
from meupacote import mod1, mod2

mod1.diga_ola()
mod2.diga_ola()
""",
}

# Criar diretórios e arquivos
for caminho, conteudo in estrutura.items():
    arquivo = base / caminho
    arquivo.parent.mkdir(parents=True, exist_ok=True)
    arquivo.write_text(conteudo)


print(
    f"""
Projeto criado em: {base.resolve()}

Rode:
python -m venv .venv
source .venv/bin/activate
cd {base / 'pkg1'} && pip install -e .
cd ../pkg2 && pip install -e .
cd ..
python teste.py
"""
)
