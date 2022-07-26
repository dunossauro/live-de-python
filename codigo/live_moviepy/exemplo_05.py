# Efeitos de audio
from moviepy.editor import AudioFileClip
from moviepy.audio.fx import all as afx

audio = (
    AudioFileClip('assets/musica_de_fundo.mp3')
    .subclip(70, 80)
    # .fx(afx.audio_fadein, 3)
    # .fx(afx.audio_fadeout, 3)
    # .fx(afx.volumex, 2)
    # .fx(afx.audio_normalize)
    .fx(afx.audio_loop, 2)
)

# print(audio.nchannels)

# audio.preview()
