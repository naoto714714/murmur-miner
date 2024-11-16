from pathlib import Path

from remove_silence import remove_silence
from speech_to_text import speech_to_text
from summary import summary

INPUT_AUDIO_FOLDER = Path("/workspaces/MurmurMiner/input_audios")
OUTPUT_SUMMARY_FOLDER = Path("/workspaces/MurmurMiner/output_summaries")
AUDIO_EXTENSIONS = [".mp3", ".wav", ".m4a"]
SAMPLING_RATE = 16000


def main():
    for audio_file in INPUT_AUDIO_FOLDER.iterdir():
        if audio_file.is_file() and audio_file.suffix.lower() in AUDIO_EXTENSIONS:
            print("----------remove_silence----------")
            no_silence_audio = remove_silence(audio_file)

            print("----------speech_to_text----------")
            transcribed_text = speech_to_text(no_silence_audio)
            print(transcribed_text)

            print("----------summary----------")
            summary_text = summary(transcribed_text)
            print(summary_text)

            output_path = OUTPUT_SUMMARY_FOLDER / f"{audio_file.stem}.txt"
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(summary_text)

            print(f"----------{audio_file}: 完了----------")


if __name__ == "__main__":
    main()
