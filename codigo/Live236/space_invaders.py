from ursina import Entity, Ursina, application, color, time
from ursina.audio import Audio
from ursina.collider import BoxCollider, SphereCollider
from ursina.input_handler import held_keys
from ursina.prefabs.editor_camera import EditorCamera
from ursina.prefabs.sky import Sky
from ursina.shaders import lit_with_shadows_shader
from ursina.text import Text
from ursina.ursinamath import clamp
from ursina.ursinastuff import destroy

app = Ursina(borderless=False)

# audios
shot = Audio('explosion.wav', autoplay=False)
died = Audio('cosmic.wav', autoplay=False)

# prefabs
Sky()
EditorCamera()


# pause
def pause_handler_input(key):
    if key == 'escape':
        application.paused = not application.paused
        pause_text.enabled = application.paused


pause_handler = Entity(ignore_paused=True)
pause_text = Text('Pausado ||', origin=(0, 0), scale=4, enabled=False)
pause_handler.input = pause_handler_input

# Game objects
class Player(Entity):
    def __init__(self):
        super().__init__()
        self.model = 'cube'
        self.color = color.green
        self.texture = 'brick'
        self.scale_y = 0.5
        self.position = (0, -3)
        self.can_shot = True
        self.shader = lit_with_shadows_shader

    def update(self):
        self.x += (
            held_keys['right arrow'] * time.dt * 5
            - held_keys['left arrow'] * time.dt * 5
        )
        self.x = clamp(self.x, -5, 5)


class Enemy(Entity):
    def __init__(self):
        super().__init__()
        self.model = 'susane'
        self.texture = 'susane_blue'
        self.scale = 0.5
        self.speed = 1
        self.rotation_y = 180
        self.collider = BoxCollider(self)
        self.shader = lit_with_shadows_shader

    def update(self):
        self.x += self.speed * time.dt
        if abs(self.x) > 5:
            self.speed *= -1
            self.y -= 1


class Bullet(Entity):
    def __init__(self, position):
        super().__init__()
        self.model = 'sphere'
        # self.color = color.yellow
        self.texture = 'grass'
        self.scale = 0.3
        self.position = position
        self.y_speed = 5
        self.collider = SphereCollider(self)
        self.shader = lit_with_shadows_shader

    def update(self):
        self.y += time.dt * self.y_speed
        if self.y > 5:
            destroy(self)
            player.can_shot = True
        if isinstance(self.intersects().entity, Enemy):
            died.play()
            destroy(self.intersects().entity)
            destroy(self)
            player.can_shot = True


# Game logic
player = Player()


def input(key):
    if key == 'space' and player.can_shot:
        Bullet(position=player.position)
        shot.play()
        player.can_shot = False


for y in range(5):
    for x in range(10):
        enemy = Enemy()
        enemy.position = (x - 4.5, y)

app.run()
