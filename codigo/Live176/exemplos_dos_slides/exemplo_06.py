"""Exemplo de como obter dados da image."""
from PIL import Image

im = Image.open('2x2px.jpg')

im.size  # (2, 2)
im.mode  # 'RGB'
im.bits  # 8

2**8  # 256
