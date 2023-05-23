from ursina import (
    Entity, Ursina, color, held_keys,
    time
)
from ursina.shaders import lit_with_shadows_shader
from ursina.lights import DirectionalLight
from ursina.audio import Audio
from ursina.prefabs.sky import Sky
from ursina.prefabs.editor_camera import EditorCamera


app = Ursina(
    borderless=False,
    fullscreen=False,
    #show_ursina_splash=True
)

Sky()
audio = Audio('explosion.wav', autoplay=False)

EditorCamera()
DirectionalLight()
susane = Entity(
    model='susane.obj',
    texture='textura.png',
    color=color.pink,
    scale=1,
    rotation=0,  # (45, 30, 19),
    position=0,  # (-5, 2, 10)
    shader=lit_with_shadows_shader
)

cubo = Entity(
    model='cube',
    texture='rainbow',
    position=(-5, 0, 0),
    shader=lit_with_shadows_shader
)

plano = Entity(
    model='plane',
    texture='grass',
    position=(0, -1, 0),
    scale=10,
    shader=lit_with_shadows_shader
)


def update():
    """Será executado 60 vezes por segundo."""
    susane.rotation_y += time.dt * 10
    susane.rotation_x += time.dt * 10
    susane.rotation_z += time.dt * 10
    susane.x += held_keys['right arrow'] * time.dt * 10
    susane.x -= held_keys['left arrow'] * time.dt * 10


app.run()
