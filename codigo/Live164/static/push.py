from browser import websocket, window, document


def on_message(evt):
    print(evt.data)
    document['message'].textContent = evt.data


def on_open(evt):
    print('Conectado')


ws = websocket.WebSocket(
    f'ws://{window.location.host}/ws/push'
)
ws.bind('message', on_message)
ws.bind('open', on_open)
