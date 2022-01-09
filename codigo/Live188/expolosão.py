from bpy.ops import (
    object, mesh
)
from bpy import context
from random import randint

# seleciona tudo
object.select_all(action='SELECT')
# deleta tudo selecionado
object.delete()

mesh.primitive_plane_add()
plano = context.object

plano.scale.x = 100
plano.scale.y = 100
object.modifier_add(type='COLLISION')


for y in range(10):
    for x in range(10):
        mesh.primitive_cube_add()
        cubo = context.object

        cubo.location.x = x * 2
        cubo.location.y = y * 2
        cubo.location.z = randint(2, 20)
        object.quick_explode(
            frame_start=2,
            frame_end=200
        )
