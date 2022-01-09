from bpy.ops import mesh, object, render
from bpy import context, data

# Remove os elementos default
object.select_all(action='SELECT')
object.delete(use_global=False, confirm=False)



def add_position_constraints(obj, target):
    """Adiciona restrições de movimentação baseados em um target."""
    object.constraint_add(type='COPY_LOCATION')
    obj.constraints["Copiar posicionamento"].target = target
    obj.constraints["Copiar posicionamento"].use_offset = True


def scene_configuration(
    scene,
    camera,
    start=0,
    end=73,
    render_path='/tmp/xpto/'
):
    """
    Faz as configurações de cena.
    
    Adiciona a câmera da cena, os frames do render e o formato de output.
    """
    scene.camera = camera
    scene.frame_start = start
    scene.frame_end = end
    scene.render.image_settings.file_format = 'FFMPEG'
    scene.render.ffmpeg.format = 'QUICKTIME'
    scene.render.ffmpeg.codec = 'PNG'
    scene.render.image_settings.color_mode = 'RGBA'
    scene.render.ffmpeg.ffmpeg_preset = 'BEST'
    scene.render.filepath = render_path
    scene.render.film_transparent = True


object.camera_add()
camera = context.object
camera.location.z = 30


# Vazio, ancora para restrição de locação
object.empty_add()
vazio = context.object
vazio.location.y = -3
vazio.location.x = -17

## Animação de posição do vazio
vazio.keyframe_insert(data_path="location", frame=0, index=0)
vazio.location.x = -8.5
vazio.keyframe_insert(data_path="location", frame=24, index=0)
vazio.keyframe_insert(data_path="location", frame=48, index=0)
vazio.location.x = -17
vazio.keyframe_insert(data_path="location", frame=72, index=0)

# Texto
object.text_add()
text = context.object
text.data.body = '@dunossauro'
text.location.x = .17
text.location.y = -0.252571
text.location.z = .01
add_position_constraints(text, vazio)

# Objeto de fundo
mesh.primitive_plane_add()
plane = context.object
plane.scale.x = 3
plane.scale.y = 0.560
plane.location.x = 3
add_position_constraints(plane, vazio)

# Lampada
object.light_add(type='AREA')
light = context.object
light.location.x = 3
light.location.z = 1.2
light.scale.x = 1.05
light.scale.y = 5.23

light.data.energy = 40
light.data.shadow_soft_size = 9.3
light.data.shape = 'RECTANGLE'
light.data.specular_factor = 0
light.data.volume_factor = 0
light.data.size = 5.78
light.data.size_y = 0.25

add_position_constraints(light, vazio)

# Materiais
black_material = data.materials.new(name='black')
black_material.use_nodes = True
black_material.node_tree.nodes[
    "Principled BSDF"
].inputs[0].default_value = (0, 0, 0, 1)

pink_material = data.materials.new(name='pink')
pink_material.use_nodes = True
pink_material.node_tree.nodes[
    "Principled BSDF"
].inputs[0].default_value = (1, 0, 0.973676, 1)

# Adionando materiais aos objetos
text.data.materials.append(black_material)
plane.data.materials.append(pink_material)


# Configurações para rederização
scene = context.scene
scene.camera = camera
scene_configuration(scene, camera)
#render.render(animation=True, use_viewport=True)
