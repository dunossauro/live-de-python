from pydub.generators import (
    Pulse,
    Sawtooth,
    Sine,
    Square,
    Triangle,
    WhiteNoise,
)
from pydub.playback import play

audioseg = Sawtooth(44_000).to_audio_segment()
audioseg = audioseg + Triangle(88_000).to_audio_segment()

play(audioseg)
