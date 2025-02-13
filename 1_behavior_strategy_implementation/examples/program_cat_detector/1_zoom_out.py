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

try:
    a = input('enter the word "yes", upper or lower case: ')
except KeyboardInterrupt:
    b = ':('
else:
    if a.lower() == 'yes':
        b = a + '!'
    else:
        b = 'baaaaad: ' + a

print(b)
