from pydub import AudioSegment

music_wav = AudioSegment.from_wav('assets/music.wav')
music_wav.fade_in().fade_out().reverse()
