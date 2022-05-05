from io import BytesIO
from shutil import copy2
from pathlib import Path
from tempfile import NamedTemporaryFile, gettempdir
from PIL import Image
from .effects import enhance_brightness, enhance_color, enhance_contrast


class Memento:
    def __init__(self):
        self.pos = 0
        self.states = []

    def last_state(self):
        return self.states[-1].copy()

    def new_state(self):
        return {
            '-CONTRASTE-': 0,
            '-BRILHO-': 0,
            '-COR-': 0,
            'path': ''
        }

    def new(self, path, window):
        self.pos = 0
        state = self.new_state()
        state['path'] = path
        self.states = [state]
        image_bytes = convert_image(path)
        window['-IMAGEM-'].update(data=image_bytes)
        self.update_sliders(state, window)

    def do(self, effect, factor, window):
        self.pos += 1
        state = self.last_state()
        path, image_bytes = apply_effect(
            effect=effect,
            factor=factor
        )
        state['path'] = path
        state[effect] = factor
        self.states.append(state)
        print(self.states)

        window['-IMAGEM-'].update(data=image_bytes)

    def update_sliders(self, state: dict, window):
        for slider in state:
            if slider != 'path':
                window[slider].update(value=state[slider])

    def undo(self, window):
        if self.pos > 0:
            self.pos -= 1
            current_state = self.states[self.pos]
            image_bytes = convert_image(current_state['path'])
            window['-IMAGEM-'].update(data=image_bytes)
            self.update_sliders(current_state, window)

    def redo(self, window):
        if self.pos < len(self.states) - 1:
            self.pos += 1
            current_state = self.states[self.pos]
            image_bytes = convert_image(current_state['path'])
            window['-IMAGEM-'].update(data=image_bytes)
            self.update_sliders(current_state, window)


meme = Memento()


def apply_effect(effect, factor):
    effects = {
        '-CONTRASTE-': enhance_contrast,
        '-BRILHO-': enhance_brightness,
        '-COR-': enhance_color,
    }
    with NamedTemporaryFile(
            prefix='ldp_', suffix='.png', delete=False
    ) as tmp_path:
        effects[effect](meme.states[meme.pos-1]['path'], factor, tmp_path)
        return tmp_path.name, convert_image(tmp_path)


def convert_image(image_path):
    image = Image.open(image_path)
    image.thumbnail((400, 400))
    bio = BytesIO()
    image.save(bio, format="PNG")
    return bio.getvalue()

def remove_all_temp():
    tmp = Path(gettempdir())

    for file in tmp.glob('ldp_*'):
        file.unlink()

def event_dispatcher(event, values, window):
    match(event):
        case '-BROWSE-':
            meme.new(values['-BROWSE-'], window)
            remove_all_temp()
        case '-CONTRASTE-' | '-BRILHO-' | '-COR-':
            meme.do(event, values[event], window)
        case '<':
            meme.undo(window)
        case '>':
            meme.redo(window)
        case None:
            remove_all_temp()
            return 'Exit'
        case 'Save As':
            copy2(meme.states[-1]['path'], values[event])
        case _:
            print('WHAT!', event, values[event])
