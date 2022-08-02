from moviepy.editor import AudioFileClip
from moviepy.audio.fx import all as afx

audio = (
    AudioFileClip('assets/musica_de_fundo.mp3')
    .subclip(60, 65)
    .fx(afx.audio_fadein, 5)
    .fx(afx.audio_fadeout, 5)
    .fx(afx.volumex, 3)
    .fx(afx.audio_normalize)
    .fx(afx.audio_loop, 3)
)

audio.preview()
