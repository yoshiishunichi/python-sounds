import scipy
from synthesizer import Synthesizer, Waveform, Writer, Player

writer = Writer()
player = Player()

synth = Synthesizer(
  osc1_waveform=Waveform.sawtooth,
  osc1_volume=1.0,
  use_osc2=True,
  osc2_waveform=Waveform.sawtooth,
  osc2_volume=0.4,
  osc2_freq_transpose=4.0,
)

wave = synth.generate_constant_wave(frequency=440.0, length=1.0)

writer.write_wave("waves/nonfilter.wav", wave)

# ローパスフィルタのパラメータ
nyquist_freq = 44100 / 2.0
cutoff_freq = 2000.0
cutoff = cutoff_freq / nyquist_freq

# ローパスフィルタを適用
n, wn = scipy.signal.buttord(cutoff, cutoff / 0.7, 6.0, 40.0)
b, a = scipy.signal.butter(n, wn)
wave = scipy.signal.filtfilt(b, a, wave)

writer.write_wave("waves/filter.wav", wave)