from pathlib import Path

from pydub import AudioSegment, silence


def cut_silences(  # https://github.com/dunossauro/videomaker-helper
    audio_file,
    output_file,
    silence_time=400,
    threshold=-65,
) -> Path:
    audio = AudioSegment.from_file(audio_file)

    silences = silence.split_on_silence(
        audio, min_silence_len=silence_time, silence_thresh=threshold
    )

    combined = AudioSegment.empty()
    for chunk in silences:
        combined += chunk

    combined.export(output_file, format='mp3')

    return Path(output_file)
