from pydub import AudioSegment
from pydub.playback import play


bass = AudioSegment.from_wav('assets/bass.wav')
pads = AudioSegment.from_wav('assets/pads.wav')
drums = AudioSegment.from_wav('assets/drums.wav')
voz = AudioSegment.from_wav('assets/abertura.wav')

music = pads[5_000: 7_000] + bass[5_000: 7_000]

music_2 = pads[5_000: 15_000].append(
    bass[5_000: 15_000], crossfade=10_000
)

music_3 = pads.overlay(bass).overlay(drums)[5_000: 20_000]

play(music_3)
