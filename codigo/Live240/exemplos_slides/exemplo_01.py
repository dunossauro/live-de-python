from textual.app import App
from textual.containers import Horizontal
from textual.widgets import Button, Footer, Header, Input, Label


class MyApp(App):
    def compose(self):
        yield Header()
        yield Label('[b]Será que clicou?[/]')
        yield Input('Digite algo!')
        with Horizontal():
            yield Button('Vermelho!', variant='error')
            yield Button('Verde!', variant='success')
            yield Button('Amarelo!', variant='warning')
        yield Footer()


MyApp().run()
