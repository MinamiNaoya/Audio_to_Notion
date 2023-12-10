import os
import matplotlib.pyplot as plt
from pydub import AudioSegment
import numpy as np


def plot_spectrogram(audio_path):
    audio = AudioSegment.from_file(audio_path)
    # audio.channelsでチャンネル数を取得しstepに指定
    
    samples = np.array(audio.get_array_of_samples())[::audio.channels]

    dt = 1.0/audio.frame_rate # サンプリング時間
    
    # 時間アレイ
    tms = 0.0
    tme = audio.duration_seconds
    tm = np.linspace(tms, tme, len(samples)) # 時間ndarrayの作成
    
    # DFT(離散フーリエ変換)
    
    N = len(samples)
    X = np.fft.fft(samples)
    f = np.fft.fftfreq(N, dt)
    
    fig, (ax01, ax02) = plt.subplots(nrows=2, figsize=(6, 8))
    plt.subplots_adjust(wspace=0.0, hspace=0.6)

    ax01.set_xlim(tms, tme)
    ax01.set_xlabel('time (s)')
    ax01.set_ylabel('x')
    ax01.plot(tm, samples) # 入力信号

    ax02.set_xlim(0, 2000)
    ax02.set_xlabel('frequency (Hz)')

    ax02.set_ylabel('|X|/N')
    ax02.plot(f[0:N//2], np.abs(X[0:N//2])/N) # 振幅スペクトル

    plt.show()

def get_audio_file_extension(file_path):
    # ファイルの拡張子を取得
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower()

def clean_audio_file(original_audio_abs_path):
    extension = get_audio_file_extension(original_audio_abs_path)
    audio = AudioSegment.from_file(original_audio_abs_path, format=extension)
    cleaned_audio = audio.low_pass_filter(1200)
    return cleaned_audio

def save_audio_file(cleaned_audio, original_audio_abs_path):
    extension = get_audio_file_extension(original_audio_abs_path)
    cleaned_audio.export(f"{original_audio_abs_path}_cleaned.{extension}", format=extension)
    