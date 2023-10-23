from pydub import AudioSegment
from pydub.playback import play

music = AudioSegment.from_wav('assets/music.wav')
play(music)
