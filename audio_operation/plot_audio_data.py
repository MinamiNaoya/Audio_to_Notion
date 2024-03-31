import matplotlib.pyplot as plt
from pydub import AudioSegment
import numpy as np

import get_audio_info

def plot_spectrogram(audio_path, segment_size=10000):
    audio = AudioSegment.from_file(audio_path)
    samples = np.array(audio.get_array_of_samples())
    for i in range(0, len(samples), segment_size):
        
        # 周波数解析を行う
        plt.figure(figsize=(12, 8))
        plt.specgram(samples, Fs=audio.frame_rate, cmap='viridis')
    
        # カラーバーの表示
        plt.colorbar(format='%+2.0f dB')
    
        # タイトル設定
        plt.title('Spectrogram')
    
        # x, y軸ラベル設定
        plt.xlabel('Time (s)')
        plt.ylabel('Frequency (Hz)')

        # プロット表示
        plt.show()