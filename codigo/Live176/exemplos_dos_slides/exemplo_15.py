from PIL import Image, ImageOps

img = Image.open('beijo_menor.jpg')

new_img = ImageOps.expand(
    img,
    border=30,
    fill='white'
)

new_img.show()
