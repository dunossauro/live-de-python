# Composição em grid
from moviepy.editor import (
    VideoFileClip,
    clips_array
)


video_0 = VideoFileClip('assets/video_0.mp4').subclip(0, 5)
video_1 = VideoFileClip('assets/video_1.mp4').subclip(0, 5)

compose = clips_array(
    [
        [video_0, video_1, video_0],
        [video_1, video_0, video_1],
    ]
)

compose.preview()
# compose.write_videofile('teste.mp4')
