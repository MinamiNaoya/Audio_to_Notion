from pydub import AudioSegment

def get_channel_count(audio_path):
    audio = AudioSegment.from_file(audio_path)
    
    channel_count = audio.channels
    return channel_count

def get_audio_duration(audio_path):
    """
    return:
        音声ファイルの長さ(秒)
    """
    # 音声ファイルを読み込む
    audio = AudioSegment.from_file(audio_path)

    # 音声ファイルの時間の長さをミリ秒で取得
    duration_in_ms = len(audio)

    # ミリ秒を秒に変換
    duration_in_sec = duration_in_ms / 1000

    return duration_in_sec


