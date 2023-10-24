from pydub import AudioSegment
from pydub.playback import play


bass = AudioSegment.from_wav('assets/bass.wav')
pads = AudioSegment.from_wav('assets/pads.wav')
drums = AudioSegment.from_wav('assets/drums.wav')
voz = AudioSegment.from_wav('assets/abertura.wav')

play(
    bass
    .overlay(pads)
    .overlay(drums - 3)[5_000: 10_000]
    .append(
        (voz[5_000:] + 10)
    .overlay(drums[5_000:] - 5), crossfade=2_000)
)
