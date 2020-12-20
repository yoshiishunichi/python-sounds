from synthesizer import Synthesizer, Waveform, Writer, Player

writer = Writer()
player = Player()
# 長3度のハモリ
synth1 = Synthesizer(
  osc1_waveform=Waveform.sine,
  osc1_volume=1.0,
  use_osc2=True,
  osc2_waveform=Waveform.sine,
  osc2_volume=0.8,
  osc2_freq_transpose=1.25
)

wave1 = synth1.generate_constant_wave(frequency=440.0, length=1)
writer.write_wave("waves/third.wav", wave1)

# 完全5度のハモリ
synth2 = Synthesizer(
  osc1_waveform=Waveform.sine,
  osc1_volume=1.0,
  use_osc2=True,
  osc2_waveform=Waveform.sine,
  osc2_volume=0.8,
  osc2_freq_transpose=1.5
)
wave2 = synth2.generate_constant_wave(frequency=440.0, length=1)
writer.write_wave("waves/fifth.wav", wave2)
