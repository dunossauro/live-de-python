from pydub import AudioSegment

bass = AudioSegment.from_wav('assets/bass.wav')

bass[1_000 * 5 :]  # Pega os primeiros cinco segundos do audio
bass[: 1_000 * 5]  # Pega após os primeiros cinco segundos
bass[1_000 * 5 :: 1_000 * 10]  # Pega entre 5 e 10 segundos
