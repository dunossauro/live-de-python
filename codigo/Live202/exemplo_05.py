from PySimpleGUIQt import (
    Window, Button, Text, Image, Input,
    Column, VSeparator, Push,
    theme, popup
)

theme('DarkPurple')

layout_direita = [
    [Image(filename='avatar.png', key='-IMAGEM-')]
]

layout_esquerda = [
    [Text('E-mail:', key='-EXEMPLO-'), Input(key='-EMAIL-')],
    [Text('Senha:'), Input(password_char='*', key='-SENHA-')],
    [
        Push(),
        Button('Login!'),
        Push(),
        Button('Esqueci a senha!'),
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

while True:
    event, values = window.read()
    print(event, values)

    match(event):  # Novidade Python 3.10
        case 'Login!':
            # popup('Login feito com sucesso')
            window['-IMAGEM-'].update(filename='avatar_2.png')
        case 'Esqueci a senha!':
            popup(f'O seu email é {values["-EMAIL-"]}')
            window['-EXEMPLO-'].update('EXEMPLO:')
        case None:
            print('Fechei, recebi None')
            break
        case _:
            print(event, values)

window.close()
