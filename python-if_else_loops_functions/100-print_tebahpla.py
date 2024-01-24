#!/usr/bin/python3

for order in range(-122, -96):
    if abs(order) % 2 == 1:
        print(chr(abs(order) - 32), end="")
    else:
        print(chr(abs(order)), end="")
