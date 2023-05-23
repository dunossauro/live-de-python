from ursina import Ursina, Entity, time

app = Ursina(borderless=False)


def rotate():
    e.rotation_z += time.dt * 45


e = Entity(model='cube', collider='box', on_click=rotate)

app.run()
