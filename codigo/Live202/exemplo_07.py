from PySimpleGUIQt import Window, Button, Text


def window_A():
    layout = [
        [Text('Janela A')],
        [Button('Janela B'), Button('Janela C')]
    ]
    return Window('Janela A', layout=layout)


def window_B():
    layout = [
        [Text('Janela B')],
        [Button('Janela A'), Button('Janela C')]
    ]
    return Window('Janela B', layout=layout)


def window_C():
    layout = [
        [Text('Janela C')],
        [Button('Janela A'), Button('Janela B')]
    ]
    return Window('Janela C', layout=layout)

window = window_A()

while True:
    event, values = window.read()

    match(event):
        case 'Janela A' | 'Janela B' | 'Janela C':
            window.close()
            match (event):
                case 'Janela A':
                    window = window_A()
                case 'Janela C':
                    window = window_C()
                case 'Janela B':
                    window = window_B()
        case None:
            break

window.close()
