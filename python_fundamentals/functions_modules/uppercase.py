#!/usr/bin/env python3
def uppercase(str):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in str:
        i = 0
        found = False
        while i < 26:
            if char == lower[i]:
                print("{}".format(upper[i]), end="")
                found = True
                break
            i += 1
        if not found:
            print("{}".format(char), end="")
    print()
