from ursina import Entity, Ursina, color
from ursina.shaders import lit_with_shadows_shader
from ursina.prefabs.editor_camera import EditorCamera
from ursina.lights import SpotLight

app = Ursina(borderless=False)
EditorCamera()

plane = Entity(
    model='plane',
    texture='white_cube',
    color=color.gray,
    scale=(10, 1, 10),
    shader=lit_with_shadows_shader,
)
cube = Entity(
    model='cube',
    texture='white_cube',
    color=color.orange,
    scale=(1, 1, 1),
    position=(0, 0.5, 0),
    shader=lit_with_shadows_shader,
)

spotlight = SpotLight(
    parent=Entity(x=1, y=5, z=1),
    rotation_x=-45,
    cutoff=45,
    outer_cutoff=50,
    shadows=True,
)

app.run()
