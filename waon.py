import scipy
from synthesizer import Synthesizer, Waveform, Writer, Player

writer = Writer()

BASE = 261.626 # C4
synth = Synthesizer(
  osc1_waveform=Waveform.sine,
  osc1_volume=1.0,
  use_osc2=False
)

# ド・ミ・ソ(C major)作成
chord = [BASE, BASE * 2.0 ** (4 / 12.0), BASE * 2.0 ** (7 / 12.0)]
wave = synth.generate_chord(chord, 1.0)
writer.write_wave("waves/C.wav", wave)

# ド・ミ♭・ソ・シ♭(Cm7)を生成
chord = [BASE, BASE * 2.0 ** (3 / 12.0), BASE * 2.0 ** (7 / 12.0), BASE * 2 ** (10 / 12.0)]
wave = synth.generate_chord(chord, 1.0)
writer.write_wave("waves/Cm7.wav", wave)
