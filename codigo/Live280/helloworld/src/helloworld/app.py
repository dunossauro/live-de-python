import toga
from toga.style.pack import COLUMN, ROW, Pack


class HelloWorld(toga.App):
    def olar(self, widget):
        self.name_output.text = f'Olar {self.name_input.value}!'

    def startup(self):
        # widgets
        name_label = toga.Label('Seu nome: ', style=Pack(padding=(0, 5)))
        self.name_input = toga.TextInput(style=Pack(flex=1))
        self.name_output = toga.Label('', style=Pack(padding=5, flex=1))
        button = toga.Button(
            'Diga oi!', on_press=self.olar, style=Pack(padding=5)
        )

        # layout widgets
        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        main_box = toga.Box(style=Pack(direction=COLUMN))
        main_box.add(name_box)
        main_box.add(button)
        main_box.add(self.name_output)

        # window
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return HelloWorld()
