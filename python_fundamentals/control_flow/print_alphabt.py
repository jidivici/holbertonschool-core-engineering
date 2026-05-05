#!/usr/bin/env python3

for i in range(97, 123):
    letter = chr(i)
    if letter not in ('e', 'q'):
        print(letter, end="")
print()
