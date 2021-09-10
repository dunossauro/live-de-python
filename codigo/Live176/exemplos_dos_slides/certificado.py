"""Exemplo do Certificado."""
from PIL import Image, ImageDraw, ImageFont

im = Image.open('certificado.jpg')

draw = ImageDraw.Draw(im)
font = ImageFont.truetype('leaguespartan-bold.ttf', size=145)

draw.text((702, 450), 'Eduardo', font=font, fill='#7ed957')
draw.text((702, 450+150), 'Mendes', font=font, fill='#7ed957')

im.show('imagem_com_texto.jpg')
