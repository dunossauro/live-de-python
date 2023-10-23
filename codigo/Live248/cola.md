# Live de Python # 248

TODOS:

- [Ouvir o podcast do jiaaro para saber da história do pydub](https://podcasts.apple.com/us/podcast/ep-27-making-your-own-luck-trust/id646591613?i=1000320317301)
- Terminar de cobrir os efeitos com exemplos
- Criar um efeito de exemplo
- Ainda faltam bons exemplos para aplicar a detecção de silêncio
- Criar os slides

## Pydub

Uma introdução

### Apresentação

[Pydub](https://github.com/jiaaro/pydub) é uma biblioteca focada em manipulação de arquivo de áudio. Seu lema é """Permitir que você faça coisas com áudio de uma forma que não seja estúpida."""

Criado por [jiaaro](https://www.jiaaro.com/) em 2011. Focada em uma API simples e de alto nível.

- Atualmente na versão 0.25.1 (lançada em março de 2021)

### Um tema subjetivo

Sei que para algumas pessoas o assunto "manipular áudio" pode parecer fora da realidade. Então, aqui vão alguns exemplos do que você pode fazer com pydub:

- Converter arquivos de áudio: .wav -> .mp3
- Cortar áudio: "5 segundos finais de uma música"
- Efeitos de transição: fade-in, fade-out, cossfade, ...
- Juntar arquivos de áudio:
  - Juntar dois áudios de 1 minuto, tendo 2 minutos de áudio
  - Juntar camadas: Dois áudios tocando ao mesmo tempo
- Separar canais de áudio: Stereo em dois canais mono
- Detecção de silêncios: "do segundo 2 ai 4.3 não tem áudio"
- Manipulação do som: Aumentar volume, abaixar volume, ...
- Obter metadados sobre o som: dBFS, duração, ...
- Tocar áudio (pydub.playback)
- Processamento de sinais: Compressão, EQ, ...
- Geração de ondas primordiais: Senoidal, Dente de serra, ruído branco ...

### O que o pydub **não faz**!

- Aplicar efeitos de plugins (VST, LV2, AU): pedalboard
- Análise de frequências e plot: Librosa
- IA: torchaudio
- Separação de instrumento: spleeter
- Transcrição de áudio (STT): whisper
- Criação de áudio por text (TTS): Coqui


### Instalação

```
pip install pydub
```


## O básico

Começando do zero!

### Seguimentos
O pydub usa um objeto primordial para tudo `AudioSegment`. Você pode importar qualquer formato de som com os métodos `from_*formato*`. Ou então usando o método `from_file(file='???', format='???')`

```python
from pydub import AudioSegment

music_wav = AudioSegment.from_wav('assets/music.wav')
music_mp3 = AudioSegment.from_mp3('assets/music.mp3')

music_mp3 = AudioSegment.from_file('assets/music.mp3', format='mp3')
```

### AudioSegment[0]

O objeto `AudioSegment` tem diversos métodos e atributos para que "você não faça coisas de maneira estúpida".

Os operadores têm funções simples e fazem com que o código seja expressivo:

```python
from pydub import AudioSegment

bass = AudioSegment.from_wav('assets/bass.wav')
pads = AudioSegment.from_wav('assets/pads.wav')

bass + 3  # Aumenta o volume em 3 dB
bass - 3  # Diminui o volume em 3 dB

bass + pads  # Adiciona os pads após o som do baixo
pads + bass  # Adiciona o baixo após o som dos pads

bass * 2  # Dobra a duração do audio, contatena o final no início
```

### AudioSegment[1]

O slice tem um papel fundamental na biblioteca para fatiar o som:

```python
from pydub import AudioSegment

bass = AudioSegment.from_wav('assets/bass.wav')

bass[1_000 * 5:]  # Pega os primeiros cinco segundos do audio
bass[:1_000 * 5]  # Pega após os primeiros cinco segundos
bass[1_000 * 5::1_000 * 10]  # Pega entre 5 e 10 segundos
```

### Tocar áudio

Embora seja uma funcionalidade focada em debug, temos como executar seguimentos de áudio:


```python
from pydub import AudioSegment
from pydub.playback import play

music = AudioSegment.from_wav('assets/music.wav')
play(music)
```


### Export

O pydub, além de obter a entrada de arquivos de áudio, também exporta os seguimentos para áudio:

```python
from pydub import AudioSegment

bass = AudioSegment.from_wav('assets/bass.wav')

bass[1_000 * 5:1_000 * 10].export('bass_5_to_10.mp3')
```

### Imutabilidade

A ideia dos seguimentos de áudio é que toda operação gere um novo seguimento:

```python
from pydub import AudioSegment

audioseg = AudioSegment.empty()
music = AudioSegment.from_wav('assets/music.wav')

new_seg = audioseg + music

new_seg.export('test.mp3')
```

### Metadados

Para obter algumas informações sobre o arquivo, como seu volume médio, seu tempo de duração, você pode solicitar essas informações para o seguimento:


```python
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
```

### Junção de áudios

Existem diversas formas de unir segmentos:

```python
from pydub import AudioSegment

seg_a = AudioSegment.from_wav('assets/bas.wav')
seg_b = AudioSegment.from_wav('assets/drums.wav')

# Adiciona um ao final do outro
seg_c = seg_a + seg_b

# Adiciona um ao final do outro com crossfade
seg_c = seg_a.append(seg_b)  # 0.1 seg
seg_c = seg_a.append(seg_b, crossfade=5000) # 5 seg de fade

# Sobrepôe os dois áudios
seg_c = seg_a.overlay(seg_b)
```

## Efeitos [WIP]

Aplicação de efeitos de áudio.

### O básico

Existem diversos efeitos que podem ser usados em seguimentos de forma básica:

- `fade()`: Aumenta ou abaixa o som progressivamente
- `fade_in`: Aumenta o som progressivamente no início
- `fade_out`: Abaixa o som progressivamente no final
- `reverse()`: Inverte a frequência do som

```python
from pydub import AudioSegment

music_wav = AudioSegment.from_wav('assets/music.wav')
music_wav.fade_in().fade_out().reverse()
```

### Efeitos

As funções de efeito são divididas em dois módulos, os oficiais do pydub `pydub.effects` e os efeitos do criados pelo scipy `pydub.scipy_effects`. Para começar vamos ver os efeitos do módulo `effects`:

- `normalize`: Normaliza o sinal para se aproximar de um valor
- `speedup`: Acelera o som em X vezes
- `strip_silence`: Remove os silêncios nas bordas
- `compress_dynamic_range`: Compressão dinâmica
- `low_pass_filter`: Foca em passar somente frequências graves
- `high_pass_filter`: Foca em passar somente frequências agudas
- `pan`: Efeito em stereo
- `apply_gain_stereo`: Aplica o ganho em um só lado


```python
from pydub import AudioSegment
from pydub.playback import play
from pydub.effects import normalize, low_pass_filter

bass = AudioSegment.from_wav('assets/bass.wav')
pads = AudioSegment.from_wav('assets/pads.wav')
drums = AudioSegment.from_wav('assets/drums.wav')
voz = normalize(AudioSegment.from_wav('assets/abertura.wav'))

music = bass.overlay(pads).overlay(drums - 3)

music_bass = low_pass_filter(music, 500)[5_000: 12_000]

play(music_bass.append(voz[:5_000], crossfade=3_000))
```

### Efeitos scipy

Para usar os efeitos do scipy, você deve instalar o `scipy`:

- `band_pass_filter`: Equalizador de duas bandas
- `eq`: Equalizador por frequência
- `low_pass_filter`: Foca em passar somente frequências graves
- `high_pass_filter`: Foca em passar somente frequências agudas


```python
from pydub import AudioSegment
from pydub.scipy_effects import eq
from pydub.playback import play

bass = AudioSegment.from_wav('assets/bass.wav')

eq_bass = eq(bass, focus_freq=500, gain_dB=-18, filter_mode='peak', order=3)[5_000:10_000]


play(eq_bass)
```

## Detecção de silêncio

Pydub conta com um módulo especializado em analisar silêncios em arquivos de áudio. Esse módulo conta com algumas funções interessantes:

- `detect_silence`: Detecta os momentos em que existem silêncios
- `detect_nonsilent`: O contrário
- `split_on_silence`: Cria uma lista de Seguimentos do som
- `detect_leading_silence`: Exibe o ms em que o silencio inicial termina

Essas funções tem quase os mesmos parâmetros:

- `min_silence_len`: Tempo mínimo para ser considerado silêncio
- `silence_thresh`: Sinal mínimo para ser considerado silêncio (basicamente o volume)

```python
from pydub import AudioSegment, silence

audioseg = AudioSegment.from_wav('assets/music.wav')

silence.detect_silence(
    audioseg, min_silence_len=500, silence_thresh=-50
)  # [[0, 4718], [48206, 52330]]

silence.detect_nonsilent(
    audioseg, min_silence_len=500, silence_thresh=-50
)  # [[4718, 48206]]

silences = silence.split_on_silence(
    audioseg, min_silence_len=500, silence_thresh=-50
)  # [<pydub.audio_segment.AudioSegment object at 0x7fcaebbe3cd0>]

silences = silence.detect_leading_silence(
    audioseg, silence_threshold=-50
)  # 4710
```


## Geradores

O pydub conta com geradores de sinal (ondas) como:

- Senoidal
- Triangular
- Quadrada
- Dente de serra
- Pulse
- Ruído branco

```python
from pydub.generators import Sawtooth, Sine, Square, Triangle, Pulse, WhiteNoise
from pydub.playback import play

audioseg = Sawtooth(44_000).to_audio_segment()
audioseg = audioseg + Triangle(88_000).to_audio_segment()

play(audioseg)
```
