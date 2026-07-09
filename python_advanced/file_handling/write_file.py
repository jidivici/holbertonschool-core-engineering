#!/usr/bin/env python3
"""Writes text to a file, overwriting any existing content."""


def write_file(filename="", text=""):
    """Writes text to the given file and returns
    the number of characters written."""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
