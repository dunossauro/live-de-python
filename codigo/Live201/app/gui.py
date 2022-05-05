from functools import partial
from PySimpleGUI import (
    Input,
    FileSaveAs,
    FileBrowse,
    Button,
    Image,
    VSeparator,
    Text,
    Column,
    Slider,
)

SliderEvent = partial(Slider, enable_events=True, default_value=1)

file_types = [('JPEG (*.jpg)', '*.jpg')]

image_side = [
    [Image(key='-IMAGEM-', size=(400, 400))],
    [
        Input(key='-BROWSE-', enable_events=True, visible=False),
        FileBrowse(target='-BROWSE-', file_types=file_types),
        Input(key='Save As', enable_events=True, visible=False),
        FileSaveAs(),
        Button('<'),
        Button('>')
    ],
]


control_side = [
    [Text('Contraste:')],
    [SliderEvent(range=(1, 5), orientation='h', key='-CONTRASTE-')],
    [Text('Brilho:')],
    [SliderEvent(range=(1, 5), orientation='h', key='-BRILHO-')],
    [Text('Cor:')],
    [SliderEvent(range=(1, 5), orientation='h', key='-COR-')],
]

layout = [[Column(image_side), VSeparator(), Column(control_side)]]
