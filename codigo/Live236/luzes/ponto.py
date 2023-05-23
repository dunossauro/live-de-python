from ursina import Entity, Ursina
from ursina.lights import PointLight
from ursina.prefabs.editor_camera import EditorCamera
from ursina.shaders import lit_with_shadows_shader

app = Ursina(borderless=False)
EditorCamera()

plano = Entity(
    model='plane',
    texture='grass',
    scale=10,
    position=(0, -1, 0),
    shader=lit_with_shadows_shader,
)
cubo = Entity(
    model='cube',
    texture='brick',
    position=(0, 1, 0),
    shader=lit_with_shadows_shader,
)

pivot = Entity()
PointLight(parent=pivot, y=4, z=3)

app.run()
