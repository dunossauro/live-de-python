from pydub import AudioSegment
from pydub.playback import play
from pydub.effects import (
    speedup, normalize, low_pass_filter, high_pass_filter
)

bass = AudioSegment.from_wav('assets/bass.wav')

voz = AudioSegment.from_wav('assets/abertura.wav')

play(
    bass[5_000: 10_000] + high_pass_filter(
        bass, 1_000
    )[5_000: 10_000] + 3
)
