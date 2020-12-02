from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

def on_press(btn):
    btn.text = 'Apertado'

def on_release(btn):
    btn.text = 'Solto!'

class MyApp(App):
    def build(self):
        box1 = BoxLayout(orientation='vertical')
        box2 = BoxLayout()

        box1.add_widget(box2)

        label = Label(text='Olar Mundo')
        label.font_size = 50

        text_input = TextInput()

        btn = Button(
            text='Butaum',
            on_press=on_press,
            on_release=on_release,
        )
        btn.font_size = 50
        
        box1.add_widget(label)
        box1.add_widget(text_input)
        box2.add_widget(btn)

        return box1


MyApp().run()
