from moviepy.editor import (
    ColorClip,
    CompositeVideoClip,
    ImageClip,
    TextClip,
    VideoFileClip,
)

video_0 = (
    VideoFileClip('personal_samples/ninja_less.mp4')
    .subclip(0, 50)
    .resize(.3)
    .margin(5)
    .set_position('right')
)
video_1 = (
    VideoFileClip('personal_samples/obs_less.mp4')
    .subclip(0, 50)
    .set_position('left')
)

image = ImageClip('personal_samples/bg.png').set_duration(video_0.duration)

text = (
    TextClip('@dunossauro', fontsize=50)
    .set_duration(video_0.duration)
    .set_position((1_480, 728))
)

color = (
    ColorClip(text.size, color=(255, 255, 255))
    .set_duration(video_0.duration)
    .set_position((1_480, 718))
)


composite = CompositeVideoClip(
    [image, video_0, video_1, color, text]
)
composite.fps = video_0.fps
composite.audio = video_1.audio

# composite.preview()
composite.write_videofile('final.mp4')
