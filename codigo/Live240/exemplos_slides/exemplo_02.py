from textual.app import App
from textual.widgets import Header, Footer, Button, Label, Input
from textual.containers import Horizontal
from textual import on


class MyApp(App):
    def compose(self):
        self.label = Label('[b]Será que clicou?[/]')
        yield Header()
        yield self.label
        yield Input('Digite algo!')

        with Horizontal():
            yield Button('Vermelho!', variant='error')
            yield Button('Verde!', variant='success')
            yield Button('Amarelo!', variant='warning')

        yield Footer()

    @on(Button.Pressed)
    def button_pressed(self, event: Button.Pressed):
        self.label.update(f'[b]Clicado no {event.button.label}[/]')

    @on(Input.Changed)
    def input_change(self, event: Input.Changed):
        self.label.update(f'[b]Texto no Input {event.input.value}[/]')

    @on(Input.Submitted)
    def input_enter(self, event: Input.Submitted):
        self.label.update(f'[b red]Texto no Input {event.input.value}[/]')


MyApp().run()
