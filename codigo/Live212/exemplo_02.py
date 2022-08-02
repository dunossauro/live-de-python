# Elementos de composição
from moviepy.editor import (
    TextClip, CompositeVideoClip, ColorClip, AudioFileClip
)


audio = AudioFileClip('assets/musica_de_fundo.mp3')

text = TextClip(
    'Dá um joinha!', color='white', fontsize=100
).set_duration(audio.duration)


color_0 = ColorClip(
    text.size, color=(255, 0, 0), duration=5
)

color_1 = ColorClip(
    text.size, color=(0, 255, 0), duration=15
)

compose = CompositeVideoClip([color_1, color_0, text])
compose.audio = audio

compose.preview()
