from pydub import AudioSegment
from pathlib import Path
import json

import audio_operate
import plot_audio_data

with open(r"audio_operation/config.json", encoding='utf-8') as f:
    config = json.load(f)
    input_abs_audiodir_path = config["device"][0]["audio_file_path"]
    is_server = config["server"][0]["is_server"]

abs_audio_file_dirpath = Path(input_abs_audiodir_path)
audio_file_name = str(input("Enter the audio file name!: "))
audio_file_path = abs_audio_file_dirpath.joinpath(audio_file_name)
print(audio_file_path)
extension = audio_operate.get_audio_file_extension

plot_audio_data.plot_spectrogram(audio_path=audio_file_path)
# cleaned_audio = audio_operate.clean_audio_file(original_audio_abs_path=audio_file_path)
# audio_operate.save_audio_file(cleaned_audio, audio_file_path)

