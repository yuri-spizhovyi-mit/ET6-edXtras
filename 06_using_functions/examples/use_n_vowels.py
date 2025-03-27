#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The program is happy if you use the correct number of vowels.

@author: Evan Cole
"""

from random import randint

from utils.count_vowels import count_vowels

expected_count = randint(1, 20)

sentence = input(f"Please enter a phrase with {expected_count} vowels.\n:  ")

actual_count = count_vowels(sentence)

if actual_count == expected_count:
    print("🙂")
else:
    print("🙁")
