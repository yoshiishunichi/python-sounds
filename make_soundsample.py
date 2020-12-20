import numpy as np
from scipy.io import wavfile
import scipy.signal

frequency = 440.0  # 生成するサイン波の周波数
seconds = 1.0      # 生成する音の秒数
rate = 44100       # 出力する wav ファイルのサンプリング周波数

phases = np.cumsum(2.0 * np.pi * frequency / rate * np.ones(int(rate * seconds)))

# 波形を生成
wave = np.sin(phases)

# 16bit の wav ファイルに書き出す
wave = (wave * float(2 ** 15 - 1)).astype(np.int16)

wavfile.write("waves/sine.wav", rate, wave)

# 鋸状波
wave = scipy.signal.sawtooth(phases)
wave = (wave * float(2 ** 15 - 1)).astype(np.int16)

wavfile.write("waves/noko.wav", rate, wave)

# 矩形波
wave = scipy.signal.square(phases)
wave = (wave * float(2 ** 15 - 1)).astype(np.int16)

wavfile.write("waves/kukei.wav", rate, wave)