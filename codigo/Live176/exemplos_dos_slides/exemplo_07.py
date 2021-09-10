"""Exemplo transformação da imagem em matriz."""
from PIL import Image
from numpy import array

im = Image.open('2x2px.jpg')

print(array(im))
"""
array([[[  0,   0,   0],
      [255, 255, 255]],

     [[255, 255, 255],
        [  0,   0,   0]]], dtype=uint8)
"""
