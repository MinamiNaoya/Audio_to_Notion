from pydub import AudioSegment
from pydub.playback import play
from pathlib import Path
import json

with open(r"audio_operation/config.json", encoding='utf-8') as f:
    config = json.load(f)
    input_abs_audiodir_path = config["device"][0]["audio_file_path"]
    is_server = config["server"][0]["is_server"]

abs_audio_file_dirpath = Path(input_abs_audiodir_path)
audio_file_name = str(input("Enter the audio file name!: "))
audio_file_path = abs_audio_file_dirpath.joinpath(audio_file_name)
print(audio_file_path)


audio = AudioSegment.from_file(audio_file_path, format="m4a")
cleaned_audio = audio.low_pass_filter(1200)

cleaned_audio.export(f"{input_abs_audiodir_path}/cleaned {audio_file_name}.wav", format="wav")

