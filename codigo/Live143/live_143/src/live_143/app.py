import toga
from functools import partial
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

def volta_box(window, widget):
    window.content = window.content


def meu_box(window, widget):
    box = toga.Box()
    box.add(
        toga.Button('voltar', on_press=partial(volta_box, window))
    )
    window.content = box
    


class live_143(toga.App):

    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)

        main_box = toga.Box()
        main_box.add(
            toga.Label(
                'Batatinha Frita',
                style=Pack(
                    font_size=50,
                    padding=50
                )
            ),
            toga.TextInput(placeholder='Sua batata preferida'),
            toga.Button('Click me', on_press=partial(meu_box, self.main_window)),
        )
        main_box.style.update(
            direction=COLUMN
        )
        
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return live_143()
