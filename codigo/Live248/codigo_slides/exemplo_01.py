from pydub import AudioSegment

bass = AudioSegment.from_wav('assets/bass.wav')
pads = AudioSegment.from_wav('assets/pads.wav')

bass + 3  # Aumenta o volume em 3 dB
bass - 3  # Diminui o volume em 3 dB

bass + pads  # Adiciona os pads após o som do baixo
pads + bass  # Adiciona o baixo após o som dos pads

bass * 2  # Dobra a duração do audio, contatena o final no início
