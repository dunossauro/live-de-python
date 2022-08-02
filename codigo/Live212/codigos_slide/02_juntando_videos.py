from moviepy.editor import VideoFileClip, concatenate_videoclips, clips_array

v1 = VideoFileClip('assets/video_0.mp4').subclip(0, 5)
v2 = VideoFileClip('assets/video_1.mp4').subclip(0, 5)


# concatenados = concatenate_videoclips([v1, v2], method='compose')
# concatenados.preview()

array = clips_array([  # Uma matriz de vídeos
    [v1, v2],  # linha 1
    [v2, v1],  # linha 2
])

array.preview()
