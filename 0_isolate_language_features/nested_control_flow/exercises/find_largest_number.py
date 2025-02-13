#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Finding the Largest Number

  Use a loop to find the largest number in a list.
"""

numbers = []

while True:
    user_input = input("Enter a number (or 'done' to finish): ")

    if user_input.lower() == __:
        break  # exit the loop

    if user_input.isdigit():  # check if the input is a number
        numbers.append(_(user_input))
    else:
        print("Invalid input, please enter a number or 'done'.")

largest = numbers[0]

for _ in _:
    if _ > largest:
        largest = _

print(f'the largest number in your list is {largest}')
