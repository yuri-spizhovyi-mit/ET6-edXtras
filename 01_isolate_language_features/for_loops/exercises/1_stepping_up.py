#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Stepping Up

Stepper Variables change systematically,
  going through a series of values for control flow

"Stepper" describes how you are using a variable
  this term is not a Python thing
  it's a general programming concept

for loops are designed for stepping
  i is the stepper in this exercise

fill in the loop condition and update the stepper variable
"""

to_repeat = "_"
total_repetitions = 4

repeated_string = ""

for _ in range(_, _, _):
    repeated_string += _

assert repeated_string == "howdyhowdyhowdyhowdy", '"howdy" should be repeated 4 times'
