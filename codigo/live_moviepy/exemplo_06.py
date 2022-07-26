# Posicionamento dinâmico
from moviepy.editor import (
    VideoFileClip, ColorClip, TextClip, CompositeVideoClip
)

def pos(time):
    return (time*50, 'center')

video_0 = VideoFileClip('assets/video_0.mp4').subclip(0, 10)
video_1 = (
    VideoFileClip('assets/video_1.mp4')
    .subclip(0, 10)
    .resize(.6)
    .set_position(('right', 'bottom'))
)

text = TextClip(
    'Live de Python', color='white', fontsize=50
).set_duration(10)

color = ColorClip(
    text.size, color=(0, 0, 0), duration=video_0.duration
)

cor_texto = CompositeVideoClip([color, text]).set_position(pos)

compose = CompositeVideoClip([video_0, video_1, cor_texto])

compose.preview()
