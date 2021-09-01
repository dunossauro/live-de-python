from os import environ
from argparse import ArgumentParser
from collections import ChainMap

defaults = {'cor': 'vermelho',
            'user': 'Convidado'}

parser = ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--cor')
parser.add_argument('-b', '--BANANAS')
namespace = parser.parse_args()
linha_comando = {k: v for k, v in vars(namespace).items()
                 if v}

combinado = ChainMap(linha_comando, environ, defaults)
print(combinado['cor'])
print(combinado['user'])
print(combinado['BANANAS'])
