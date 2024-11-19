# 参考：https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0
# 参考：https://huggingface.co/docs/transformers/model_doc/whisper#transformers.WhisperForConditionalGeneration
# 参考：https://qiita.com/ryosuke_ohori/items/9634c1fd8a9cc9ff7c36
import torch
from transformers import WhisperForConditionalGeneration, WhisperProcessor

from utils import measure_time


@measure_time
def speech_to_text(audio, sampling_rate):
    model_id = "kotoba-tech/kotoba-whisper-v2.0"
    device = "cuda" if torch.cuda.is_available() else "cpu"

    processor = WhisperProcessor.from_pretrained(model_id)
    model = WhisperForConditionalGeneration.from_pretrained(model_id).to(device)

    input_features = processor(
        audio,
        return_tensors="pt",
        truncation=False,
        padding="longest",
        return_attention_mask=True,
        sampling_rate=sampling_rate,
    ).input_features.to(device)

    generated_ids = model.generate(input_features, return_timestamps=True)
    return processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
