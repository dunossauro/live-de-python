from PySimpleGUI import Window, Button, Text

layout = [
    [Button('Botão 1'), Button('Coluna 1')],  # Linha 1
    [Button('Botão 2')],  # Linha 2
    [Text('Aperte o botão 3:'), Button('Botão 3')],  # Linha 3
]

window = Window(
    'Janela da Live de Python',
    layout=layout
)

print(window.read())

window.close()
