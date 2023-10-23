from pydub import AudioSegment
from pydub.effects import low_pass_filter, normalize
from pydub.playback import play

bass = AudioSegment.from_wav('assets/bass.wav')
pads = AudioSegment.from_wav('assets/pads.wav')
drums = AudioSegment.from_wav('assets/drums.wav')
voz = normalize(AudioSegment.from_wav('assets/abertura.wav'))

music = bass.overlay(pads).overlay(drums - 3)

music_bass = low_pass_filter(music, 500)[5_000:12_000]

play(music_bass.append(voz[:5_000], crossfade=3_000))
