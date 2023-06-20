from textual import on
from textual.app import App
from textual.containers import Container
from textual.widgets import Label, Header, Footer, Input, Button
from textual.events import Key, MouseScrollUp


class MyApp(App):
    TITLE = 'Meu APP TOP!!!!!'

    CSS_PATH = 'style.css'

    BINDINGS = [
        # O atalho, Action, Mensagem do footer
        ('t', 'change_theme()', 'Muda o tema'),
        ('s', 'sair()', 'Sai da aplicação'),
        ('f', 'find_buttons()', 'Loga os botões')
    ]

    def action_change_theme(self):
        self.dark = not self.dark

    def action_sair(self):
        self.exit()

    def compose(self):
        yield Header(show_clock=True)
        with Container(classes='label'):
            yield Label(
                'Boas vindas a Live de Python # 240',
                id='texto'
            )
        yield Input('Digite algo')

        with Container(classes='buttons'):
            yield Button('Verde!', variant='success', id='verde')
            yield Button(
                'Amarelo!', variant='warning', classes='amarelo'
            )
            yield Button(
                'Vermelho!', variant='error', classes='amarelo'
            )

        yield Footer()

    def action_find_buttons(self):
        for b in self.query('Button'):
            self.log('***action_find_buttons***', b)

    @on(Button.Pressed, '#verde')
    def butao_verde(self, event: Button.Pressed):
        self.query_one('#texto').update(
            f'Texto: [green b]{event.button.label}[/]'
        )

    @on(Button.Pressed, '.amarelo')
    def butao_amarelo(self, event: Button.Pressed):
        self.query_one('#texto').update(
            f'Texto: [yellow b]{event.button.label}[/]'
        )
        

    def on_input_changed(self, event: Input.Changed):
        self.query_one('#texto').update(f'Texto: {event.input.value}!')

    def on_input_submitted(self, event: Input.Submitted):
        self.query_one('#texto').update(
            f'Texto: [red b]{event.input.value}[/]!'
        )

    def on_key(self, event: Key):
        self.log('Evento on_key: ***** ', event.key)

    def on_mouse_scroll_up(self, event: MouseScrollUp):
        self.log('Evento de scroll: ***** ', event)


MyApp().run()
