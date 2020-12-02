from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from plyer import vibrator, battery, notification

class MyBoxLayout(BoxLayout):
    propriedade = StringProperty('0')

    def notificar(self, *args):
        notification.notify('Titulo', 'Notificação')

    def bateria(self, *args):
        self.propriedade = str(battery.status['percentage']) + '%'

    def vibrar(self, *args):
        vibrator.vibrate(2)

    def mudar(self, *args):
        self.propriedade = '10'

    def request(self, *args):
        def on_success(req, response):
            self.propriedade = str(response)

        def on_error(req, response):
            self.propriedade = 'Deu ruim! ' + str(response)

        def on_failure(req, response):
            self.propriedade = 'Deu ruim2! ' + str(response)

        self.request = UrlRequest(
            'https://pokeapi.co/api/v2/pokemon/ditto',
            on_success=on_success,
            on_error=on_error,
            on_failure=on_failure,
            verify=False
        )
        
        print(self.request)


class MainApp(App):
    def build(self):
        return MyBoxLayout()


MainApp().run()
