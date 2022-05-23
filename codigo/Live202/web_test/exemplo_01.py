# exemplo_01.py
from PySimpleGUIWeb import (
    Button, Image, Input, Text, Window,
)

layout = [
    [Image(filename='avatar.png')],
    [Text('E-mail'), Input()],
    [Text('Senha'), Input(password_char='*')],
    [Button('Login!'), Button('Esqueci a senha!')],
]


window = Window(
    'Tela de Login',
    layout=layout,
    element_justification='c'
)

print(window.read())

window.close()
