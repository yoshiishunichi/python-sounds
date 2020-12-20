from synthesizer import Synthesizer, Waveform, Writer, Player

synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)

# 一定音程の波形を生成
wave = synth.generate_constant_wave(frequency=440.0, length=1.0)

# オーディオファイル出力
writer = Writer()
writer.write_wave("waves/sine.wav", wave)

# オーディオデバイス出力
player = Player()
player.open_stream()

# デバイスの一覧を表示
player.enumerate_device()

# 出力デバイスを指定可能
# player.open_stream(device_name="UA-25EX")

player.play_wave(wave)