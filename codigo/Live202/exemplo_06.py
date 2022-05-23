from PySimpleGUI import Window, FileBrowse

layout = [
    [FileBrowse(enable_events=True)]
]


window = Window('Exemplo PlayGround', layout=layout)

print(window.read())

window.close()
