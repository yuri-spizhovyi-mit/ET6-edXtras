#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A program that quizzes the user on the nth number in the Fibonacci sequence.

@author: Evan Cole
"""

from random import randint

from utils.fibonacci_list import fibonacci_list

index = randint(0, 99)

guess = int(input(f'What number is step {index} in the Fibonacci sequence?  \n:  '))

actual = fibonacci_list(index).pop()

if guess == actual:
    print(f'Correct! \n{guess} is step {index}')
else:
    print(f'Nope :( \n{actual} is step {index}, not {guess}.')
