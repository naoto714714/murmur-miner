from pathlib import Path

from remove_silence import remove_silence

INPUT_AUDIO_FOLDER = Path("/workspaces/MurmurMiner/input_audios")
OUTPUT_FOLDER = Path("/workspaces/MurmurMiner/output_files")
ONLY_SPEECH_FOLDER = "only_speech"
AUDIO_EXTENSIONS = [".mp3", ".wav", ".m4a"]


def main():
    for audio_file in INPUT_AUDIO_FOLDER.iterdir():
        if audio_file.is_file() and audio_file.suffix.lower() in AUDIO_EXTENSIONS:
            remove_silence(audio_file, f"{OUTPUT_FOLDER}/{ONLY_SPEECH_FOLDER}")
            print(f"処理完了: {audio_file.name}")


if __name__ == "__main__":
    main()
