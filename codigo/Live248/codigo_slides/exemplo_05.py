from pydub import AudioSegment

audioseg = AudioSegment.empty()
music = AudioSegment.from_wav('assets/music.wav')

new_seg = audioseg + music

new_seg.export('test.mp3')
