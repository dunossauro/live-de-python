# Efeitos parte 1
from moviepy.editor import VideoFileClip
from moviepy.video.fx import all as vfx

# Padrão de projeto, Builder

v0 = (
    VideoFileClip('assets/video_0.mp4')
    .subclip(0, 10)
    # .rotate(180)
    # .fadein(4)
    # .fadeout(4)
    # .speedx(10)
    .resize(2)
    # .fx(vfx.accel_decel, 10)
    # .fx(vfx.blackwhite)
    # .fx(vfx.colorx, .8)
    # .fx(vfx.invert_colors)
    # .fx(vfx.margin, 20)
    # .fx(vfx.loop, 2)
    # .fx(vfx.make_loopable, 1)
)

v0.preview()
