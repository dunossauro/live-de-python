from textual.app import App
from textual.widgets import Header, Footer, Button, Label, Input
from textual.containers import Container
from textual.events import Key, Click, MouseScrollUp, MouseScrollDown


class MyApp(App):
    TITLE = 'Meu aplicativo TOP!'
    CSS_PATH = 'teste.css'
    BINDINGS = [
        ('t', 'change_theme()', 'Muda o tema!'),
        ('s', 'exit()', 'Sai da aplicação!'),
        ('b', 'show_all_buttons()', 'Mostra todos os botões!'),
    ]

    def action_change_theme(self):
        self.dark = not self.dark

    def action_exit(self):
        self.exit()

    def compose(self):
        yield Header()
        with Container(classes='label'):
            yield Label('[b]Será que clicou?[/]', id='label')
        yield Input('Digite algo!')

        with Container(classes='buttons'):
            yield Button('Vermelho!', variant='error')
            yield Button('Verde!', variant='success')
            yield Button('Amarelo!', variant='warning')

        yield Footer()

    def action_show_all_buttons(self):
        for element in self.query('Button'):
            self.log('Botão', element.label)

    def on_button_pressed(self, event: Button.Pressed):
        self.query_one('#id').update(f'[b]Clicado no {event.button.label}[/]')

    def on_input_changed(self, event: Input.Changed):
        try:
            self.query_one('#id').update(f'[b]Texto no Input {event.input.value}[/]')
        except:
            # O evento acontece antes de montar a interface!
            ...

    def on_input_submitted(self, event: Input.Submitted):
        self.query_one('#id').update(f'[b red]Texto no Input {event.input.value}[/]')

    def on_key(self, event: Key):
        self.log(f'on_key {event.key} foi precionada', event=event)

    def on_click(self, event: Click):
        self.log('on_click', event=event)

    def on_mouse_scroll_up(self, event: MouseScrollUp):
        self.log('on_mouse_scroll_up', event=event)

    def on_mouse_scroll_down(self, event: MouseScrollDown):
        self.log('on_mouse_scroll_down', event=event)


MyApp().run()
