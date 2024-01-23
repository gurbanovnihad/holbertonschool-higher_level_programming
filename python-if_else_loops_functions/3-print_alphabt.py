#!/usr/bin/python3
for order in range(ord('a'), ord('z') + 1):
    letter = chr(order)
    if letter == 'q' or letter == 'e':
        continue
    else:
        print("{}".format(letter), end='')
