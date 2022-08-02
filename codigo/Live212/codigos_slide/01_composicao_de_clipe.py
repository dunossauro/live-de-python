"""
Vídeo clip com muitos elementos compostos em um único clip

.write_videofile() -> renderiza o vídeo
"""
from moviepy.editor import (
    AudioFileClip,
    ColorClip,
    CompositeVideoClip,
    TextClip,
    VideoFileClip
)

video = VideoFileClip('assets/video_0.mp4').subclip(0, 5)
video2 = (
    VideoFileClip('assets/video_1.mp4')
    .subclip(0, 5)
    .resize(0.3)
    .set_position(('right', 'top'))
)
audio = AudioFileClip('assets/musica_de_fundo.mp3').subclip(100, 105)

texto = (
    TextClip('Live de Python', color='white', fontsize=50)
    .set_duration(5)
    .set_position((10, 'bottom'))
)

quadrado = (
    ColorClip(size=texto.size, color=(0, 0, 0), duration=5)
    .set_position((8, video.h - texto.h - 6))
)

composição = CompositeVideoClip(
    # Lista de coisas que serão compostas
    [video, video2, quadrado, texto]
)
composição.audio = audio

composição.write_videofile('teste.mp4')
