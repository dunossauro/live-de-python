"""Exemplo rotacionando a matriz em 90 graus."""
from PIL import Image
from numpy import array, rot90

im = Image.open('2x2px.jpg')


Image.fromarray(   # Nova imagem
    rot90(         # Rotaciona a matriz em 90
        array(im)  # matriz
    )
).show()
