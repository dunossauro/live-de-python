from moviepy.editor import ColorClip, VideoFileClip, CompositeVideoClip

def pos(tempo):
    return (tempo*30, 10)
    

video = VideoFileClip('assets/video_0.mp4').subclip(0, 5)

color = ColorClip(
    (200, 200), color=(0, 0, 0), duration=video.duration
).set_position(pos)



comp = CompositeVideoClip([video, color])

comp.preview()
