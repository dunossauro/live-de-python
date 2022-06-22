from time import sleep
from os import getenv

from httpx import get
from dotenv import load_dotenv
from PySimpleGUI import (
    DEFAULT_FONT,
    Button,
    Image,
    Input,
    PopupAnimated,
    Text,
    Window,
    theme,
)
from sqlalchemy import (
    Column,
    Integer,
    LargeBinary,
    String,
    create_engine,
    select,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

engine = create_engine(getenv('DATABASE'))
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Pokemon(Base):
    __tablename__ = 'Pokemon'

    id = Column(Integer, primary_key=True)
    name = Column('name', String(32))
    image = Column('image', LargeBinary())


Base.metadata.create_all(engine)
session = Session()

splash_image = getenv('SPLASH')

if splash_image:
    PopupAnimated(
        splash_image,
        location=(300, 200)
    )
    sleep(3)
    PopupAnimated(None)

layout = [
    [
        Input(key='-INPUT-', font=(DEFAULT_FONT, 30)),
        Button('Image!', font=(DEFAULT_FONT, 30)),
    ],
    [Text(key='-NAME-', font=(DEFAULT_FONT, 30))],
    [Image(key='-IMAGE-')],
]


def request_pokemon(number):
    URL = f'{getenv("POKE_API")}{number}/'
    response = get(URL).json()

    name = response['name']

    image_url = response['sprites']['other']['home']['front_default']
    image = get(image_url).content

    return name, image


def search_on_db(id):
    query = select(Pokemon).where(Pokemon.id == id)
    return session.execute(query).scalars().all()


def put_on_db(id, name, image):
    Poke = Pokemon(id=id, name=name, image=image)
    session.add(Poke)
    session.commit()


theme('DarkAmber')

window = Window(
    'Pokedex', layout=layout, location=(10, 300), element_justification='c'
)

while True:
    event, value = window.read()
    if event is None:
        break
    if event == 'Image!':
        db_values = search_on_db(value['-INPUT-'])

        if not db_values:
            name, image = request_pokemon(value['-INPUT-'])
            put_on_db(value['-INPUT-'], name, image)
        else:
            poke = db_values[0]
            image = poke.image
            name = poke.name

        window['-IMAGE-'].update(data=image)
        window['-NAME-'].update(name)


session.close()
