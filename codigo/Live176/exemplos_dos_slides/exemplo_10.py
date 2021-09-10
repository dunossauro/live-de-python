"""Exemplo melhorias de Contraste."""
from PIL import Image, ImageEnhance

im = Image.open('beijo.jpg')

contrast = ImageEnhance.Contrast(im)
contrast.enhance(1.2)

contrast.show()
