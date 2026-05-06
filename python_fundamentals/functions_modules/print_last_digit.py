#!/usr/bin/env python3

def print_last_digit(number):
    last = number % 10
    return last if number >= 0 else (10 - last if last != 0 else 0)

