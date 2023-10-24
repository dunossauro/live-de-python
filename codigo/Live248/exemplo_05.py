from pydub import AudioSegment
from pydub.generators import (
    Sine,
    Sawtooth,
    WhiteNoise,
    Square,
    Triangle,
    Pulse,
)
from pydub.playback import play

vazio = AudioSegment.empty()

senoides = sum(
    [Sawtooth(x * 1_000).to_audio_segment() for x in [11, 22, 44, 88, 160]]
)

play(senoides)
