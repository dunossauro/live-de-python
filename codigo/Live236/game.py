# Space invaders
from ursina import (
    Entity, Ursina, color, held_keys,
    time, clamp, Sky, EditorCamera, SphereCollider,
    BoxCollider, destroy, Audio
)
from ursina.shaders import lit_with_shadows_shader


app = Ursina()

shot = Audio('explosion.wav', autoplay=False)
died = Audio('cosmic.wav', autoplay=False)

Sky()
EditorCamera()

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.model = 'cube'
        self.color = color.green
        self.texture = 'brick'
        self.scale_y = .5
        self.position = (0, -3)
        self.shader = lit_with_shadows_shader
        self.can_shot = True

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
        self.texture = 'textura.png'
        self.scale = .5
        self.position = (0, -3)
        self.rotation_y = 180
        self.speed = 1
        self.shader = lit_with_shadows_shader
        self.collider = BoxCollider(self)

    def update(self):
        self.x += self.speed * time.dt
        if abs(self.x) > 5:
            self.speed *= -1
            self.y -= 1

class Bullet(Entity):
    def __init__(self, position):
        super().__init__()
        self.model = 'sphere'
        self.texture = 'grass'
        self.scale = .3
        self.position = position
        self.collider = SphereCollider(self)
        self.shader = lit_with_shadows_shader
        self.speed = 5

    def update(self):
        self.y += time.dt * self.speed
        if self.y > 5:
            destroy(self)
            player.can_shot = True
        if isinstance(
            self.intersects().entity, Entity
        ):
            destroy(self.intersects().entity)
            destroy(self)
            died.play()
            player.can_shot = True

player = Player()

def input(key):
    if key == 'space' and player.can_shot:
        Bullet(player.position)
        shot.play()
        player.can_shot = False


for y in range(5):
    for x in range(10):
        enemy = Enemy()
        enemy.position = (x - 4.5, y)

app.run()
