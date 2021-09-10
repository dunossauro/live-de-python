from PIL import Image, ImageEnhance, ImagePalette

image = Image.open('beijo.jpg')
image = image.resize((1280, 720))


saturation = ImageEnhance.Color(image)
contrast = ImageEnhance.Contrast(image)
brightness = ImageEnhance.Brightness(image)
sharpness = ImageEnhance.Sharpness(image)


# for x in range(0, 5, 1):
#     saturation.enhance(x).show(f'{x}')
#     contrast.enhance(x).show(f'{x}')
#     brightness.enhance(x).show(f'{x}')
#     sharpness.enhance(x).show(f'{x}')


def my_filter(img):
    contrast = ImageEnhance.Contrast(img)
    contrastado = contrast.enhance(1.1)
    brightness = ImageEnhance.Brightness(contrastado)
    brilho = brightness.enhance(1.1)
    saturation = ImageEnhance.Color(brilho)
    saturada = saturation.enhance(1.3)
    arcoiro = Image.open('vinheta.png')
    saturada.paste(arcoiro, (0, 0), arcoiro)
    saturada.show()
    ImagePalette.sepia(saturada).show()
    saturada.save('beijo_vinheta.png')


my_filter(image)
