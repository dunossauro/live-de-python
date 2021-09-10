"""Exemplo de redimensionamento da imagem."""
from PIL import Image

# Abre a imagem
im = Image.open('beijo.jpg')

tamanho = (1280, 720)  # x, y

# Gera um novo objeto Image
im_menor = im.resize(tamanho)

im_menor.show('Minha imagem!')

im_menor.save('beijo_menor.jpg')
