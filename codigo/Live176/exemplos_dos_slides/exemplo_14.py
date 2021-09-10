"""Exemplo de fonte customizada."""
from PIL import Image, ImageDraw, ImageFont

im = Image.open('beijo_menor.jpg')

draw = ImageDraw.Draw(im)
font = ImageFont.truetype('Abys-Regular.otf', size=150)

draw.text((10, 10), 'Live de Python!', font=font)


im.show('imagem_com_texto.jpg')
