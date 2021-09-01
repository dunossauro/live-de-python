# Errado
import sys, os

# Certo
import os
import sys

# ORDEM DOS IMPORTS
# proximas implementaões
import __future__

# biblioteca padrão
import os
import sys

# biblioteca de terceiros
import requests
import funcy

# bibliotecas proprias
import minha_lib
import minha_outra_lib


# Imports com wildcard
# Errado
from re import *
fildall(r'\w+', 'eduardo foi a escola')

# Certo
from re import findall
fildall(r'\w+', 'eduardo foi a escola')


# Imports que sobreescrevem funções builtins
# ERRADO
from re import *                  # NOQA
from re import compile            # NOQA
compile() # Default ou import?    # NOQA

# CERTO
import re                                      # NOQA
from re import compile as re_compile           # NOQA
re_compile()                                   # NOQA
re.compile()                                   # NOQA
