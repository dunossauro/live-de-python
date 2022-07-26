from moviepy.editor import VideoFileClip
from moviepy.video.fx import all as vfx

video = (
    VideoFileClip('assets/video_0.mp4')
    # .subclip(0, 30)
    .fx(vfx.accel_decel, 2)  # Acelera o vídeo
    # .fx(vfx.blackwhite)      # Vídeo preto e branco
    .fx(vfx.colorx, 1.2)      # Multiplica as cores por um fator (.4)
    # .fx(vfx.crop, x1=100)    # Recorta um pedaço do clip (x1 e y1 superior esquerdo, x2 e y2 direito)
    # .fx(vfx.fadein, 3)       # Fade in
    # .fx(vfx.fadeout, 3)      # Fade out
    # .fx(vfx.freeze, 3, 2)    # Dá freeze no segundo 3 por 2 segundos
    # .fx(vfx.gamma_corr, 2)      # Correção de gamma
    .fx(vfx.invert_colors)      # Inverte as cores
    .fx(vfx.loop, 3)            # Clipe em loop por X vezes
    # .fx(vfx.lum_contrast, 3, 5) # Contraste e luma
    .fx(vfx.make_loopable, 3)   # Faz o fim misturar com o começo
    .fx(vfx.margin, 10)         # Margem em torno do vídeo
    # .fx(vfx.speedx, 10)         # Acelera o vídeo
)

# video.rotate(180)

video.preview()
