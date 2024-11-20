# 参考：https://github.com/snakers4/silero-vad/wiki/Examples-and-Dependencies#examples
from silero_vad import collect_chunks, get_speech_timestamps, load_silero_vad, read_audio

from utils import measure_time


@measure_time
def remove_silence(audio_file, sampling_rate):
    model = load_silero_vad(onnx=False)
    audio = read_audio(audio_file, sampling_rate=sampling_rate)

    speech_timestamps = get_speech_timestamps(audio, model, sampling_rate=sampling_rate)

    return collect_chunks(speech_timestamps, audio)
