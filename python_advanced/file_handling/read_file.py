#!/usr/bin/env python3
"""Reads and returns the content of a file."""

def read_file(filename=""):
    """Opens and returns the full content of the given file."""
    with open(filename, mode="r") as f:
        return f.read()
