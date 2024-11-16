# 参考：https://github.com/snakers4/silero-vad/wiki/Examples-and-Dependencies#examples
from silero_vad import collect_chunks, get_speech_timestamps, load_silero_vad, read_audio, save_audio

from main import SAMPLING_RATE


def remove_silence(audio_file):
    model = load_silero_vad(onnx=False)
    audio = read_audio(audio_file, sampling_rate=SAMPLING_RATE)

    speech_timestamps = get_speech_timestamps(audio, model, sampling_rate=SAMPLING_RATE)

    return collect_chunks(speech_timestamps, audio)
