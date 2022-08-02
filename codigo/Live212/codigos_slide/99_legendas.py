from datetime import timedelta
from json import loads
from pathlib import Path
import wave
from srt import Subtitle, compose
from pydub import AudioSegment
from vosk import Model, KaldiRecognizer, SetLogLevel

SetLogLevel(-1)

entrada = 'personal_samples/drummond.mp4'
saida = 'drummond.wav'
legenda = 'personal_samples/drummond.str'
model_path = Path('~/documents/vosk/vosk-model-small-pt-0.3')
WORDS_PER_LINE = 7
model = Model(str(model_path.expanduser()))


audio = AudioSegment.from_file(entrada, 'mp4')
audio = audio.set_channels(1)
audio = audio.set_frame_rate(16000)
audio.export(saida, format='wav')


wf = wave.open(saida, 'rb')
rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)

results = []
subs = []

while True:
    data = wf.readframes(4_000)

    if len(data) == 0:
        break

    if rec.AcceptWaveform(data):
        result = rec.Result()
        results.append(result)
        print(result)

results.append(rec.FinalResult())


for i, res in enumerate(results):
    jres = loads(res)
    if not 'result' in jres:
        continue
    words = jres['result']
    for j in range(0, len(words), WORDS_PER_LINE):
        line = words[j: j + WORDS_PER_LINE]
        s = Subtitle(
            index=len(subs),
            content=' '.join([l['word'] for l in line]),
            start=timedelta(seconds=line[0]['start']),
            end=timedelta(seconds=line[-1]['end'])
        )
        subs.append(s)

with open(legenda, 'w') as file:
    file.write(compose(subs))
