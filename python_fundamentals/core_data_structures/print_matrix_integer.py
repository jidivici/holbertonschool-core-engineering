#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in range(len(row)):
            end_char = ", " if element != len(row) - 1 else ""
            print("{}".format(row[element]), end=end_char)
        print()
