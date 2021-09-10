"""Exemplo de como virar[flip] imagems."""
from PIL import Image

# Abre a imagem
im = Image.open('beijo_menor.jpg')

# Flip
im.transpose(Image.FLIP_LEFT_RIGHT).show()  # Invete na horizontal
im.transpose(Image.FLIP_TOP_BOTTOM).show()  # Invete na vertical

# Transposição
im.transpose(Image.ROTATE_90).show()
im.transpose(Image.ROTATE_180).show()
im.transpose(Image.ROTATE_270).show()
im.transpose(Image.TRANSPOSE).show()
im.transpose(Image.TRANSVERSE).show()
