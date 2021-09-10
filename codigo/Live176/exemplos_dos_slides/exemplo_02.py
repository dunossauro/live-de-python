"""Exemplo de conversão do tipo da imagem."""
from PIL import Image

# Abre a imagem
im = Image.open('beijo.jpg')

# Mostra a imagem
im.show('Minha imagem!')

# Salva a imagem em png
im.save('exemplo.png')
