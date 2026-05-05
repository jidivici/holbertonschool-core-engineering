#!/usr/bin/env python3
def uppercase(str):
    new_str = ""
    for char in str:
        if 'a' <= char <= 'z':
            new_char = chr(ord(char) - 32)
        else:
            new_char = char
        new_str += new_char
    return new_str
