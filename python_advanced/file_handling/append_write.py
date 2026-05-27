#!/usr/bin/env python3
"""Appends text to a file."""


def append_write(filename="", text=""):
    """Appends text to the given file and returns
    the number of characters written."""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
