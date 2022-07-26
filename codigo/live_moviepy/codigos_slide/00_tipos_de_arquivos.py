"""
Tipos de dados primordiais para edição de vídeo

Durações:
    - Video: .subclip()
    - Audio: .subclip()
    - Audio: .subclip()
    - Text:  .set_duration()
    - Color: duration=
    - image: duration=

.preview() - Necessita do pygame instalado [opcional]
"""
from moviepy.editor import (
    AudioFileClip,
    ColorClip,
    ImageClip,
    TextClip,
    VideoFileClip
)

video = VideoFileClip('assets/video_0.mp4').subclip(0, 5)

audio = AudioFileClip('assets/musica_de_fundo.mp3').subclip(100, 105)

texto = TextClip('Live de Python', color='white', fontsize=50).set_duration(5)

cor = ColorClip(size=video.size, color=(255, 255, 0), duration=5)

imagem = ImageClip('image.png', duration=5)

video.preview()
# audio.preview()
# texto.preview()
# cor.preview()
# imagem.preview()

## Atributos de vídeo
video.size      # Dimensões do Clip
video.duration  # Duração do clip em segundos
video.fps       # Frames por segundo
# Um iterador frame a frame (matriz de imagem)
video.iter_frames

## Atributos de áudio
audio.fps        # Frequência do audio
audio.duration   # Duração do audio em segundos
audio.nchannels  # Número de canais (1 - mono, 2 - stereo)

## Atributos de imagem
imagem.duration  # Tempo do clip de imagem
image.size       # Dimensões da imagem
image.img        # Matriz da imagem
