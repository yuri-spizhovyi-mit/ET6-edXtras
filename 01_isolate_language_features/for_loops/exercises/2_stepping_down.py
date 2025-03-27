#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Stepping Down

Stepper Variables change systematically,
  going through a series of values for control flow

"Stepper" describes how you are using a variable
  this term is not a Python thing
  it's a general programming concept

for loops are designed for stepping
  i is the stepper in this exercise

fill in the loop condition and update the stepper variable
"""

holiday = "winter solstice"
message = "_" + holiday

tweet = ""
for days_to_holiday in range(_, _, _):
    tweet = str(days_to_holiday) + message

assert tweet == "1 days remaining until winter solstice", "there are 0 days remaining"
