import os
import shutil
from glob import glob
from os import path

if path.exists('desafio_2'):
    shutil.rmtree('desafio_2')

os.mkdir('desafio_2')


for file in glob('files/pasta_0/*.txt'):
    shutil.copy(file, 'desafio_2')
