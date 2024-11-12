# 参考：https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0#short-form-transcription
import torch
from transformers import pipeline


def speech_to_text(audio_path):
    # config
    model_id = "kotoba-tech/kotoba-whisper-v2.0"
    torch_dtype = torch.bfloat16 if torch.cuda.is_available() else torch.float32
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    model_kwargs = {"attn_implementation": "sdpa"} if torch.cuda.is_available() else {}
    generate_kwargs = {"language": "ja", "task": "transcribe"}

    # load model
    pipe = pipeline(
        "automatic-speech-recognition",
        model=model_id,
        torch_dtype=torch_dtype,
        device=device,
        model_kwargs=model_kwargs,
    )

    # run inference
    result = pipe(audio_path, return_timestamps=True, generate_kwargs=generate_kwargs)
    return result["text"]