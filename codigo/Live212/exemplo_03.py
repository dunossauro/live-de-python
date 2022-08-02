# Elementos de composição
from moviepy.editor import (
    AudioFileClip,
    VideoFileClip,
    concatenate_videoclips
)

audio = AudioFileClip('assets/musica_de_fundo.mp3')
v0 = VideoFileClip('assets/video_0.mp4').subclip(0, 5)
v1 = VideoFileClip('assets/video_1.mp4').subclip(0, 5)

compose = concatenate_videoclips([v0, v1, v0, v0], method='compose')
audio = audio.subclip(0, compose.duration)
compose.audio = audio

compose.write_videofile('teste.mp4')
