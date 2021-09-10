"""Exemplo de aplicação de realces."""
from PIL import Image, ImageEnhance

image = Image.open('beijo_menor.jpg')

saturation = ImageEnhance.Color(image)
contrast = ImageEnhance.Contrast(image)
brightness = ImageEnhance.Brightness(image)
sharpness = ImageEnhance.Sharpness(image)


def duno_filtro(img):
    contrast = ImageEnhance.Contrast(img)
    contrastado = contrast.enhance(1.1)

    brightness = ImageEnhance.Brightness(contrastado)
    brilho = brightness.enhance(1.1)

    saturation = ImageEnhance.Color(brilho)
    saturada = saturation.enhance(1.3)

    vinheta = Image.open('vinheta.png')
    saturada.paste(vinheta, (0, 0), vinheta)

    saturada.save('beijo_editada.jpg')


duno_filtro(image)
