#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A program that challenges the user to guess the index of a Fibonacci number.

@author: Evan Cole
"""

from random import randint

from utils.fibonacci_list import fibonacci_list

actual = randint(0, 99)

number = fibonacci_list(actual).pop()

guess = int(input(f'What is the index of {number} in the Fibonacci sequence?  \n:  '))

if guess == actual:
    print(f'Correct! \n{number} has index {guess}.')
else:
    print(f'Nope :( \n{number} has index {actual}, not {guess}.')
