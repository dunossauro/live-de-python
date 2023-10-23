from pydub import AudioSegment

music_wav = AudioSegment.from_wav('assets/music.wav')
music_mp3 = AudioSegment.from_mp3('assets/music.mp3')

music_mp3: AudioSegment = AudioSegment.from_file(
    'assets/music.mp3', format='mp3'
)
