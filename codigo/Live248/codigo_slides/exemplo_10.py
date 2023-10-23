from pydub import AudioSegment
from pydub.scipy_effects import eq
from pydub.playback import play

bass = AudioSegment.from_wav('assets/bass.wav')

eq_bass = eq(
    bass, focus_freq=500, gain_dB=-18,
    filter_mode='peak', order=3
)[5_000:10_000]


play(eq_bass)
