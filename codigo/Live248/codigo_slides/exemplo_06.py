from pydub import AudioSegment

seg = AudioSegment.from_wav('assets/music.wav')

# Informações gerais
seg.duration_seconds  # Duração
seg.raw_data  # O Array
seg.channels  # Quantidade de canais
seg.frame_rate  # framerate

# Informações sobre amplitude
seg.rms       # Loudness
seg.dBFS      # Loudness logarítimo
seg.max_dBFS  # Maior amplitude em dB
seg.max  # Maior amplitude

# Informações sobre frames
seg.frame_count  # Número de frames
seg.frame_width  # Número de bytes em frames
seg.sample_width  # Número de bytes por sample
