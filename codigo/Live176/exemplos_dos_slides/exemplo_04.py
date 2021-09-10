"""Exemplo de rotação da imagem."""
from PIL import Image

# Abre a imagem
im = Image.open('beijo_menor.jpg')


# Rotaciona a imagem e perde o que extiver fora do tamanho original
angulo = 45  # Positivos para direita, Negativos esquerda
im.rotate(angulo).show()  # Matém o tamanho da imagem
im.rotate(angulo, expand=True).show()  # Expande para caber
im.transpose(Image.TRANSPOSE).show()  # Gira a imagem
