from ursina import (
    Entity, Ursina, color, held_keys,
    time
)
from ursina.shaders import lit_with_shadows_shader
from ursina.lights import DirectionalLight
from ursina.prefabs.sky import Sky
from ursina.prefabs.editor_camera import EditorCamera
from ursina.audio import Audio
from ursina.collider import MeshCollider


app = Ursina(
    borderless=False,
    fullscreen=False,
)

Sky()
EditorCamera()
DirectionalLight()
audio = Audio('explosion.wav', autoplay=False)

def click_susane():
    susane_a.rotation_y += time.dt * 35
    susane_a.rotation_x += time.dt * 35
    susane_a.rotation_z += time.dt * 35

class Susane(Entity):
    def __init__(self, pos_x=0, pos_z=0):
        super().__init__()
        self.model = 'susane.obj'
        self.texture = 'textura.png'
        self.color = color.pink
        self.scale = 1
        self.position = (pos_x, 0, pos_z)
        self.shader = lit_with_shadows_shader
        self.on_click = click_susane
        self.collider = MeshCollider(self)

    def update(self):
        """Será executado 60 vezes por segundo."""
        # self.rotation_y += time.dt * 10
        # self.rotation_x += time.dt * 10
        # self.rotation_z += time.dt * 10
        self.x += held_keys['right arrow'] * time.dt * 10
        self.x -= held_keys['left arrow'] * time.dt * 10


plano = Entity(
    model='plane',
    texture='grass',
    position=(0, -1, 0),
    scale=10,
    shader=lit_with_shadows_shader
)

susane_a = Susane()
susane_b = Susane(1, 1)

def input(key):
    if key == 'space':
        audio.play()

app.run()
