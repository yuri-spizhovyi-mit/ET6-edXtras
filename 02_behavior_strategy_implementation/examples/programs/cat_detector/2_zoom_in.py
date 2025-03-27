#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
A user can input anything, if the input is "yes" the program is excited
- given the user interrupts (Ctrl+C), the program is sad
- given the user inputs 'yes' (case insensitive) the program is excited
- given any other inputs, the program says it's "baaaaad"

Test cases:
- the user interrupts
  KeyboardInterrupt -> ':('
- any sort of 'yes'
  'yes' -> 'yes!'
  'Yes' -> 'Yes!'
  'yES' -> 'yES!'
- any other input
  'hello' -> 'baaaaad: hello'
  '' -> 'baaaaad: '
  'good bye' -> 'baaaaad: good bye'
"""

# try-except block: handle potential keyboard interrupt
try:
    # call input(): get string from user
    # declare, init: store user's input as string
    a = input('enter the word "yes", upper or lower case: ')
except KeyboardInterrupt:
    # assign: sad face for interrupted input
    b = ":("
else:
    # check: convert input to lower case and compare to 'yes'
    if a.lower() == "yes":
        # assign: the input concatenated with exclamation mark
        b = a + "!"
    else:
        # assign: baaaad concatenated with the input
        b = "baaaaad: " + a

# call print: show the final b
print(b)
