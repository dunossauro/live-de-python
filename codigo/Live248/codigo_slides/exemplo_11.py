from pydub import AudioSegment, silence

audioseg = AudioSegment.from_wav('assets/music.wav')

silence.detect_silence(
    audioseg, min_silence_len=500, silence_thresh=-50
)  # [[0, 4718], [48206, 52330]]

silence.detect_nonsilent(
    audioseg, min_silence_len=500, silence_thresh=-50
)  # [[4718, 48206]]

silences = silence.split_on_silence(
    audioseg, min_silence_len=500, silence_thresh=-50
)  # [<pydub.audio_segment.AudioSegment object at 0x7fcaebbe3cd0>]

silences = silence.detect_leading_silence(
    audioseg, silence_threshold=-50
)  # 4710
