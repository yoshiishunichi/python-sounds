from synthesizer import Synthesizer, Waveform, Writer, Player
from getch import getch, pause


# 半音のズレが何倍か定義
onestep_pitch = 2 ** (1.0 / 12.0)
# 音を鳴らす時間をmsで定義
duration = 300

# 音を鳴らす関数を定義
def play_pitch(frequency, duration):

  synth = Synthesizer(
    osc1_waveform=Waveform.sawtooth, # 1つ目のオシレータの波形
    osc1_volume=1.0, # 1つ目のオシレータのボリューム
    use_osc2=True, #2つ目のオシレータの有無
    osc2_waveform=Waveform.sine, #2つ目のオシレータの波形
    osc2_volume=0.6, #2つ目のオシレータのボリューム
    osc2_freq_transpose=2.0 # 2つ目のオシレータの周波数の比率
  )
  wave = synth.generate_constant_wave(frequency=frequency, length=1.0 * (duration / 1000))
  player = Player()
  player.open_stream()
  player.play_wave(wave)

# 半音上げ下げする関数
def down_pitch(base_pitch):
  return int(round(base_pitch / onestep_pitch))

def up_pitch(base_pitch):
  return int(round(base_pitch * onestep_pitch))

# 各音程の周波数を定義

# 1段目
A4 = 440
Gis4 = down_pitch(A4)
G4 = down_pitch(Gis4)
Fis4 = down_pitch(G4)
F4 = down_pitch(Fis4)
E4 = down_pitch(F4)
Dis4 = down_pitch(E4)
D4 = down_pitch(Dis4)
Cis4 = down_pitch(D4)
C4 = down_pitch(Cis4)
Ais4 = up_pitch(A4)
B4 = up_pitch(Ais4)

# 2段目
C5 = up_pitch(B4)
Cis5 = up_pitch(C5)
D5 = up_pitch(Cis5)
Dis5 = up_pitch(D5)
E5 = up_pitch(Dis5)
F5 = up_pitch(E5)
Fis5 = up_pitch(F5)
G5 = up_pitch(Fis5)
Gis5 = up_pitch(G5)
A5 = up_pitch(Gis5)
Ais5 = up_pitch(A5)
B5 = up_pitch(Ais5)

# 3段目
C6 = up_pitch(B5)
Cis6 = up_pitch(C6)
D6 = up_pitch(Cis6)
Dis6 = up_pitch(D6)
E6 = up_pitch(Dis6)
F6 = up_pitch(E6)
Fis6 = up_pitch(F6)
G6 = up_pitch(Fis6)
Gis6 = up_pitch(G6)
A6 = up_pitch(Gis6)
Ais6 = up_pitch(A6)
B6 = up_pitch(Ais6)

# キーボードと音程を関連づける。キーボードの"d"がC4、つまりドの音など
pitchs = {}
pitchs["1"] = C4
pitchs["2"] = Cis4
pitchs["3"] = D4
pitchs["4"] = Dis4
pitchs["5"] = E4
pitchs["6"] = F4
pitchs["7"] = Fis4
pitchs["8"] = G4
pitchs["9"] = Gis4
pitchs["0"] = A4
pitchs["-"] = Ais4
pitchs["^"] = B4

pitchs["q"] = C5
pitchs["w"] = Cis5
pitchs["e"] = D5
pitchs["r"] = Dis5
pitchs["t"] = E5
pitchs["y"] = F5
pitchs["u"] = Fis5
pitchs["i"] = G5
pitchs["o"] = Gis5
pitchs["p"] = A5
pitchs["@"] = Ais5
pitchs["["] = B5

pitchs["a"] = C6
pitchs["s"] = Cis6
pitchs["d"] = D6
pitchs["f"] = Dis6
pitchs["g"] = E6
pitchs["h"] = F6
pitchs["j"] = Fis6
pitchs["k"] = G6
pitchs["l"] = Gis6
pitchs[";"] = A6
pitchs[":"] = Ais6
pitchs["]"] = B6


while True:
  key = getch()
  key = key.lower()
  print(key)
  if key in pitchs:
    play_pitch(pitchs[key], duration)
  elif key == "_":
    break