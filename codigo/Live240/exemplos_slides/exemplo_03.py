from textual.app import App
from textual.widgets import Header, Footer, Button, Label, Input
from textual.containers import Horizontal
from textual.events import Key, Click, MouseScrollUp, MouseScrollDown


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

    def on_button_pressed(self, event: Button.Pressed):
        self.label.update(f'[b]Clicado no {event.button.label}[/]')

    def on_input_changed(self, event: Input.Changed):
        self.label.update(f'[b]Texto no Input {event.input.value}[/]')

    def on_input_submitted(self, event: Input.Submitted):
        self.label.update(f'[b red]Texto no Input {event.input.value}[/]')

    def on_key(self, event: Key):
        self.log(f'on_key {event.key} foi precionada', event=event)

    def on_click(self, event: Click):
        self.log('on_click', event=event)

    def on_mouse_scroll_up(self, event: MouseScrollUp):
        self.log('on_mouse_scroll_up', event=event)

    def on_mouse_scroll_down(self, event: MouseScrollDown):
        self.log('on_mouse_scroll_down', event=event)


MyApp().run()
