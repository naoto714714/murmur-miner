# 参考：https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0#short-form-transcription
# 参考：https://qiita.com/ryosuke_ohori/items/9634c1fd8a9cc9ff7c36
import torch
from transformers import WhisperForConditionalGeneration, WhisperProcessor


def speech_to_text(audio, sampling_rate):
    model_id = "kotoba-tech/kotoba-whisper-v2.0"
    device = "cuda" if torch.cuda.is_available() else "cpu"

    processor = WhisperProcessor.from_pretrained(model_id)
    model = WhisperForConditionalGeneration.from_pretrained(model_id).to(device)

    input_features = processor(audio, sampling_rate=sampling_rate, return_tensors="pt").input_features.to(device)

    generated_ids = model.generate(input_features)
    return processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
