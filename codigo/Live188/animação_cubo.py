from bpy import context, data
from bpy.ops import render
from math import radians


cena = context.scene
cena.frame_start = 0
cena.frame_end = 48

cubo = context.object
cubo.location.x = 0
cubo.rotation_euler.x = 0

pink_material = data.materials.new(name='pink')
pink_material.use_nodes = True
pink_material.node_tree.nodes[
    "Principled BSDF"
].inputs[0].default_value = (1, 0, 0.973676, 1)

cubo.data.materials.append(pink_material)

cubo.keyframe_insert(
    data_path='location',
    frame=0
)

cubo.keyframe_insert(
    data_path='rotation_euler',
    frame=0
)


cubo.location.x = 10
cubo.keyframe_insert(
    data_path='location',
    frame=24
)

cubo.location.x = 0

cubo.keyframe_insert(
    data_path='location',
    frame=48
)

cubo.rotation_euler.x = radians(45)
cubo.keyframe_insert(
    data_path='rotation_euler',
    frame=48
)

cena.render.image_settings.file_format = 'FFMPEG'
cena.render.ffmpeg.format = 'QUICKTIME'
cena.render.ffmpeg.codec = 'PNG'
cena.render.image_settings.color_mode = 'RGBA'
cena.render.film_transparent = True
# render.render(animation=True)