#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Multiplication Grid

    Nested loops can generate a multiplication table
    The outer loop controls the row, and the inner loop fills the row

    examples:
    
        rows: 3, columns: 3 ->
            0 0 0
            0 1 2
            0 2 4

        rows: 5, columns: 4 ->
            0 0 0 0
            0 1 2 3
            0 2 4 6
            0 3 6 9 
            0 4 8 12
"""

# --- declare helper function ---

def get_int_from_user(message: str) -> int:
    while True:
        user_input = input(message)

        if user_input.isdigit():
            user_int = int(user_input)
            break
        else:
            print("Invalid input, please enter an integer.")

    return user_int


# --- main program ---


rows = get_int_from_user('how many rows do you want in the grid?  ')
columns = get_int_from_user('how many columns do you want in the grid?  ')

grid = ''
for _ in range(_): 
    row = ""
    for _ in range(_): 
        _ += str(_ * _) + " " 
    _ += row + '\n'

print(grid)
