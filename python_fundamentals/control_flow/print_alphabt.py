#!/usr/bin/env python3

alphabet = "abcdefghijklmnopqrstuvwxyz"
i = 0

while i < len(alphabet):
    if alphabet[i] != 'e' and alphabet[i] != 'q':
        print(alphabet[i], end="")
    i += 1

print()
