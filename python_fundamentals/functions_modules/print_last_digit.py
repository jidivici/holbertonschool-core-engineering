#!/usr/bin/env python3

def print_last_digit(number):
    if number < 0:
        new_number = -abs(number) % 10
    else:
        new_number = abs(number) % 10
    print(new_number)
    return new_number
