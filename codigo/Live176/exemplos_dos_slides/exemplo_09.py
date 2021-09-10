"""Exemplo modos de pixel."""
from PIL import Image
from numpy import array

im = Image.open('2x2px.jpg')

array(im.convert('1'))  # True / False
array(im.convert('L'))  # 0 - 255
array(im.convert('P'))  # 0 - 255
array(im.convert('RGB'))
