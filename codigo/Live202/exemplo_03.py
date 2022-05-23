from PySimpleGUI import (
    Window, Button, Text, Image, Input,
    Column, VSeparator, Push
)

layout_direita = [
    [Image(filename='avatar.png')]
]

layout_esquerda = [
    [Text('E-mail:'), Input()],
    [Text('Senha:'), Input(password_char='*')],
    [
        Push(),
        Button('Login!'),
        Push(),
        Button('Esqueci a senha'),
        Push(),
    ],
]

layout = [
    [Column(layout_direita), VSeparator(), Column(layout_esquerda)]
]

window = Window(
    'Janela da Live de Python',
    layout=layout,
)

print(window.read())

window.close()
