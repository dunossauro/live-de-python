from ursina import Entity, Ursina
from ursina.lights import AmbientLight
from ursina.prefabs.editor_camera import EditorCamera
from ursina.shaders import lit_with_shadows_shader

app = Ursina(borderless=False)

cubo = Entity(model='cube', texture='brick', shader=lit_with_shadows_shader)
plano = Entity(
    model='plane',
    texture='grass',
    scale=10,
    position=(0, -1, 0),
    shader=lit_with_shadows_shader,
)

light = AmbientLight()

EditorCamera()

app.run()
