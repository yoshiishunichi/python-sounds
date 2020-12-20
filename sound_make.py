from synthesizer import Synthesizer, Waveform, Writer, Player

synth = Synthesizer(
  osc1_waveform=Waveform.sawtooth, # 1つ目のオシレータの波形
  osc1_volume=1.0, # 1つ目のオシレータのボリューム
  use_osc2=True, #2つ目のオシレータの有無
  osc2_waveform=Waveform.sine, #2つ目のオシレータの波形
  osc2_volume=0.6, #2つ目のオシレータのボリューム
  osc2_freq_transpose=2.0 # 2つ目のオシレータの周波数の比率
)

writer = Writer()
wave = synth.generate_constant_wave(frequency=440.0, length=1.0)
writer.write_wave("waves/overtone.wav", wave)

player = Player()
player.open_stream()


synth2 = Synthesizer(
  osc1_waveform=Waveform.sawtooth, # 1つ目のオシレータの波形
  osc1_volume=1.0, # 1つ目のオシレータのボリューム
  use_osc2=False #2つ目のオシレータの有無
)
wave2 = synth.generate_constant_wave(frequency=220.0, length=1.0)
writer.write_wave("waves/overtone.wav", wave2)
player.play_wave(wave)
player.play_wave(wave2)