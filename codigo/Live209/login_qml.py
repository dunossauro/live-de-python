from PySide6.QtCore import QObject, Slot
from pathlib import Path
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtGui import QGuiApplication

from httpx import get

class Ponte(QObject):
    @Slot(str, result=list)
    def fetch_image(self, pokemon_id):
        image_path = Path('pokemon_image.png')
        try:
            if image_path.exists():
                print('Deletando imagem')
                image_path.unlink()

            response = get(
                f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
            ).json()

            image_url = response['sprites']['other']['home']['front_default']
            image_content = get(image_url).content

            with open('pokemon_image.png', 'wb') as poke_image:
                poke_image.write(image_content)
        except Exception as e:
            print(e)
        finally:
            return str(image_path), response['name'].capitalize() + '!'

app = QGuiApplication()

engine = QQmlApplicationEngine()
engine.load('login_qml.qml')

ponte = Ponte()
context = engine.rootContext()
context.setContextProperty('ponte', ponte)

app.exec()
