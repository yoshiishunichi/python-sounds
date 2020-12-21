from pychord import Chord

c = Chord("C")
am7 = Chord("Am7")
slash = Chord("F/G")

print("c:", c.components())
print("am7:", am7.components())
print("slash:", slash.components())