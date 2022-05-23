# from PySimpleGUI import Window, Text, Input, Button, Image, theme
# from PySimpleGUIQt import Window, Text, Input, Button, Image, theme
from PySimpleGUIWeb import Window, Text, Input, Button, Image, theme
# from PySimpleGUIWx import Window, Text, Input, Button, Image, theme

# ---- Temas
# from PySimpleGUI import theme_previewer
# theme_previewer()
# ----

theme('DarkPurple')

layout = [
    [Image(filename='avatar.png', size=(400, 400))],
    [Text('E-mail:'), Input()],  # Linha 1
    [Text('Senha:'), Input()],  # Linha 2
    [Button('Login!'), Button('Esqueci a senha!')],
]

window = Window(
    'Tela de Login',
    layout=layout,
    element_justification='c'
)

while True:
    event, values = window.read()
    if event is None:
        break
    if event:
        print(event, values)

window.close()
