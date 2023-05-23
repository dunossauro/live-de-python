from ursina import Entity, time, Ursina
from ursina.input_handler import held_keys
from ursina.prefabs.editor_camera import EditorCamera
from ursina.shaders import lit_with_shadows_shader

app = Ursina(borderless=False)
EditorCamera()

e = Entity(model='sphere', texture='grass')

class Cubo(Entity):
    def __init__(self):
        super().__init__()
        self.model = 'cube'
        self.texture = 'brick'
        self.shader = lit_with_shadows_shader
      
    def update(self):
        self.rotation_z += time.dt * 20
        self.x += held_keys['right arrow'] * time.dt * 5
        self.x -= held_keys['left arrow'] * time.dt * 5

cubo = Cubo()

def update():
    e.rotation_z += time.dt * 20
    e.y += held_keys['up arrow'] * time.dt * 5
    e.y -= held_keys['down arrow'] * time.dt * 5

app.run()
