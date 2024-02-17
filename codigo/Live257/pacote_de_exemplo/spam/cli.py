import os

from InquirerPy import inquirer
from InquirerPy.validator import PathValidator
from rich.console import Console
from rich_pixels import Pixels
from typer import Typer

console = Console()
app = Typer()


@app.command()
def main():
    src_path = inquirer.filepath(
        message='Encontre sua imagem:',
        default='.',
        validate=PathValidator(is_file=True, message='Input is not a file'),
        only_files=True,
    ).execute()

    pixels = Pixels.from_image_path(src_path, (100, 100))
    console.print(pixels)
