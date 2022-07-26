from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.fx import all as vfx
from pydub import AudioSegment, silence

file = 'personal_samples/drummond.mp4'


def cut_silences(clip) -> list:
    audio = AudioSegment.from_file(clip.filename, 'mp4')

    silences = silence.detect_silence(
        audio,
        min_silence_len=1_000,
        silence_thresh=-45,
    )

    cuts = []
    last = 0
    for i, (start, stop) in enumerate(silences):
        if i % 2:
            subclib = clip.subclip(last, start/1000).fx(vfx.blackwhite)
        else:
            subclib = clip.subclip(last, start/1000)
        if subclib.duration:
            cuts.append(subclib)
        last = stop/1000

    final_subclib = clip.subclip(last, video.duration)
    cuts.append(final_subclib)

    return cuts


video = VideoFileClip(file)
cuts = cut_silences(video)
compose = concatenate_videoclips(cuts, method='compose')
compose.write_videofile('teste.mp4')
