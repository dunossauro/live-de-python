from pydub import AudioSegment

seg_a = AudioSegment.from_wav('assets/bas.wav')
seg_b = AudioSegment.from_wav('assets/drums.wav')

# Adiciona um ao final do outro
seg_c = seg_a + seg_b

# Adiciona um ao final do outro com crossfade
seg_c = seg_a.append(seg_b)  # 0.1 seg
seg_c = seg_a.append(seg_b, crossfade=5000)  # 5 seg de fade

# Sobrepôe os dois áudios
seg_c = seg_a.overlay(seg_b)
