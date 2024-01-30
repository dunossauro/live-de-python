from PySimpleGUI import Window
from app.events import event_dispatcher
from app.gui import layout


window = Window('LDP Photo', layout)

while True:  # Eventloop
    event, values = window.read()

    event_result = event_dispatcher(event, values, window)

    if event_result == 'Exit':
        break

window.close()
