#!/usr/bin/python3

for order in range(-122, -96):
    if abs(order) % 2 == 1:
        print("{}".format(chr(abs(order) - 32)), end="")
    else:
        print("{}".format(chr(abs(order))), end="")
