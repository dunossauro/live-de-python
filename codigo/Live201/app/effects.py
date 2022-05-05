from PIL import Image
from PIL import ImageEnhance


def enhance_contrast(image_path, enhance_factor, output_path):
    image = Image.open(image_path)
    enhancer = ImageEnhance.Contrast(image)
    new_image = enhancer.enhance(enhance_factor * 0.1 + 1)
    new_image.save(output_path)


def enhance_color(image_path, enhance_factor, output_path):
    image = Image.open(image_path)
    enhancer = ImageEnhance.Color(image)
    new_image = enhancer.enhance(enhance_factor * 0.1 + 1)
    new_image.save(output_path)


def enhance_brightness(image_path, enhance_factor, output_path):
    image = Image.open(image_path)
    enhancer = ImageEnhance.Brightness(image)
    new_image = enhancer.enhance(enhance_factor * 0.1 + 1)
    new_image.save(output_path)
