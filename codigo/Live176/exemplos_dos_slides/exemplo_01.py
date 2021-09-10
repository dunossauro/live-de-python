"""Exemplos iniciais e básicos para toda e qualquer imagem."""
from PIL import Image

# Abre a imagem
im = Image.open('beijo.jpg')

# Mostra a imagem
im.show('Minha imagem!')

# Salva a imagem
im.save('exemplo.jpg')
