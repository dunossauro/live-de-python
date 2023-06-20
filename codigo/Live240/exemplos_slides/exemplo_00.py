from textual.app import App
from textual.widgets import Label


class MyApp(App):
    def compose(self):
        yield Label('Olá Mundo!')


MyApp().run()
