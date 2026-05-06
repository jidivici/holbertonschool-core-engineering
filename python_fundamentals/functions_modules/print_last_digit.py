#!/usr/bin/env python3

def print_last_digit(number):
    last = number % 10
    if number < 0 and last != 0:
        last = 10 - last
    return last
