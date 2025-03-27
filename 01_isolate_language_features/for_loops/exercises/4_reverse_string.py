#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Reverse strings

you can use for loops to do some logic for each element in a string

this loop should create a new string with the letters from the original reversed
"""

original_string = "abcde"

reversed_string = ""

for _ in original_string:
    next_letter = _
    reversed_string = _

    print(_)  # your stepper variable

assert reversed_string == "edcba", "reversed string is the original reversed"
