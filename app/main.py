import sys
from pathlib import Path

from remove_silence import remove_silence
from speech_to_text import speech_to_text
from summary import summary

INPUT_AUDIO_FOLDER = Path("/workspaces/MurmurMiner/input_audios")
OUTPUT_SUMMARY_FOLDER = Path("/workspaces/MurmurMiner/output_summaries")
AUDIO_EXTENSIONS = [".mp3", ".wav", ".m4a"]
SAMPLING_RATE = 16000


def main():
    audio_files = check_audio_files()
    if not audio_files:
        print("音声ファイルが見つかりません。入力可能なファイル形式: mp3, wav, m4a")
        sys.exit(1)

    for audio_file in audio_files:
        print(f"----------remove_silence: {audio_file}----------")
        no_silence_audio = remove_silence(audio_file, SAMPLING_RATE)

        print(f"----------speech_to_text: {audio_file}----------")
        transcribed_text = speech_to_text(no_silence_audio, SAMPLING_RATE)
        print(transcribed_text)

        print(f"----------summary: {audio_file}----------")
        summary_text = summary(transcribed_text)
        print(summary_text)

        output_path = OUTPUT_SUMMARY_FOLDER / f"{audio_file.stem}.txt"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(summary_text)

        print(f"----------完了: {audio_file}----------")

    sys.exit(0)


def check_audio_files():
    audio_files = [f for f in INPUT_AUDIO_FOLDER.iterdir() if f.is_file() and f.suffix.lower() in AUDIO_EXTENSIONS]
    return audio_files


if __name__ == "__main__":
    main()
