from pydub import AudioSegment

def get_channel_count(audio_path):
    audio = AudioSegment.from_file(audio_path)
    
    channel_count = audio.channels
    return channel_count


