from PySimpleGUI import (
    Window, Button, Text, Image, Input,
)

layout = [
    [Image(filename='avatar.png')],
    [Text('E-mail:'), Input()],
    [Text('Senha:'), Input(password_char='*')],
    [Button('Login!'), Button('Esqueci a senha')],
]

window = Window(
    'Janela da Live de Python',
    layout=layout,
)

print(window.read())

window.close()
