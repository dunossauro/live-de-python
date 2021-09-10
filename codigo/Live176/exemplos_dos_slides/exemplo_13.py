"""Exemplo de um texto Simple"""
from PIL import Image, ImageDraw

im = Image.new(  # Cria uma nova imagem
    'RGB', (200, 200), 'green'
)

draw = ImageDraw.Draw(im)
draw.text((10, 10), 'Live de Python!')


im.show('imagem_com_texto.jpg')
