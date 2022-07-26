from moviepy.editor import (
    AudioFileClip,
    VideoFileClip,
    ImageClip,
    CompositeVideoClip
)


video = VideoFileClip('assets/video_0.mp4').subclip(0, 5).resize(2)

audio = AudioFileClip('assets/musica_de_fundo.mp3').subclip(50, 55)

image = ImageClip(
    'assets/2022-07-24-13-51-42-image.png', duration=5
)

compose = CompositeVideoClip([video, image])
compose.audio = audio

# compose.preview()
compose.write_videofile('teste.mp4')
