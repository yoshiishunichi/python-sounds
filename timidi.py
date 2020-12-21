from midi import sequencer as sequencer
hardware = sequencer.SequencerHardware()
for client in hardware._clients:
    print(client)
# MIDIデバイス名が出力される
# TiMidity
# Midi Through