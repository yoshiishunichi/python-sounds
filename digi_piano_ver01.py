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

# 2段目
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


# 1段目
B3 = down_pitch(C4)
Ais3 = down_pitch(B3)
A3 = down_pitch(Ais3)
Gis3 = down_pitch(A3)
G3 = down_pitch(Gis3)
Fis3 = down_pitch(G3)
F3 = down_pitch(Fis3)
E3 = down_pitch(F3)
Dis3 = down_pitch(E3)
D3  = down_pitch(Dis3)
Cis3 = down_pitch(D3)
C3 = down_pitch(Cis3)


# 3段目
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


# キーボードと音程を関連づける。
pitchs = {}
pitchs["1"] = C3
pitchs["2"] = Cis3
pitchs["3"] = D3
pitchs["4"] = Dis3
pitchs["5"] = E3
pitchs["6"] = F3
pitchs["7"] = Fis3
pitchs["8"] = G3
pitchs["9"] = Gis3
pitchs["0"] = A3
pitchs["-"] = Ais3
pitchs["^"] = B3

pitchs["q"] = C4
pitchs["w"] = Cis4
pitchs["e"] = D4
pitchs["r"] = Dis4
pitchs["t"] = E4
pitchs["y"] = F4
pitchs["u"] = Fis4
pitchs["i"] = G4
pitchs["o"] = Gis4
pitchs["p"] = A4
pitchs["@"] = Ais4
pitchs["["] = B4

pitchs["a"] = C5
pitchs["s"] = Cis5
pitchs["d"] = D5
pitchs["f"] = Dis5
pitchs["g"] = E5
pitchs["h"] = F5
pitchs["j"] = Fis5
pitchs["k"] = G5
pitchs["l"] = Gis5
pitchs[";"] = A5
pitchs[":"] = Ais5
pitchs["]"] = B5


while True:
  key = getch()
  key = key.lower()
  print(key)
  if key in pitchs:
    play_pitch(pitchs[key], duration)
  elif key == "_":
    break