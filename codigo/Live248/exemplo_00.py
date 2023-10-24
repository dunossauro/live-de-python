from pydub import AudioSegment
from pydub.playback import play


bass = AudioSegment.from_wav('assets/bass.wav')
pads = AudioSegment.from_wav('assets/pads.wav')

corte_baixo = bass[5_000: 7_000]
corte_teclado = pads[5_000: 7_000]

# + int (aumenta o volume)
# - int (abaixa o volume)
# * int (tona N vezes)
# audiosegment + audiosegment (concatena segmentos)

# [de onde: até onde] - ms

musica = (
    corte_baixo * 3 + corte_teclado * 2 + corte_baixo
)

musica.export('musica_bolada.mp3')

musica_bolada = AudioSegment.from_mp3('musica_bolada.mp3')

play(musica_bolada)

# play(bass + pads)
