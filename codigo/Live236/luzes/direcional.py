from ursina import Entity, Ursina
from ursina.lights import DirectionalLight
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

pivot = Entity(rotation_x=45, rotation_y=45)
DirectionalLight(parent=pivot, y=2, z=3, shadows=True)

app.run()
