from pydub import AudioSegment, silence
from pydub.playback import play

audio = AudioSegment.from_file(
    'output.wav'
)


silencio = AudioSegment.empty()

silencios = silence.detect_nonsilent(
    audio,
    min_silence_len=100,
    silence_thresh=-65
)

for start, stop in silencios:
    silencio += audio[start - 50: stop + 50]

# play(audio)
play(silencio)
