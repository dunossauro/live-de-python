from pydub import AudioSegment

bass = AudioSegment.from_wav('assets/bass.wav')

bass[1_000 * 5 : 1_000 * 10].export('bass_5_to_10.mp3')
