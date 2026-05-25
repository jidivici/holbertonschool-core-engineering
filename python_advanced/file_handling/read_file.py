#!/usr/bin/env python3

def read_file(filename=""):
    with open(filename, mode="r") as f:
        return f.read()
