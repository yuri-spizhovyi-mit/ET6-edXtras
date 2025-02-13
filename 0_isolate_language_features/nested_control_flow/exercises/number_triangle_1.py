#!/usr/bin/env python3
# -*- coding: utf-8 -*-


""" Number Triangle

   Use nested loops to generate a triangle of numbers.

   examples:

        2 -> 
        1 
        2 2 

        4->
        1 
        2 2 
        3 3 3 
        4 4 4 4
"""


while True:
    user_input = input("how many rows should the pyramid have?:  ")

    if user_input.isdigit():
        rows = int(user_input)
        break
    else:
        print("Invalid input, please enter a number.")


pyramid = ''

for _ in range(_): 
    row = ""
    for _ in range(_ + 1):
        row += str(_) + " "
    pyramid += _ + '\n'

print(pyramid)
