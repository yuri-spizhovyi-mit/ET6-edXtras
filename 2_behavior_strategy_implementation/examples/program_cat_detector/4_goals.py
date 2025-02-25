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

# --- gather user input safely ---

# try-except block: handle potential keyboard interrupt
# this structure ensures we handle all possible ways the user might interact
try:
    # call input(): get string from user
    # declare, init: store user's input as string
    #   this line explains to the user what they need to input
    #   the user_input variable is used later to check if they entered valid input
    user_input = input('enter the word "yes", upper or lower case: ')
except KeyboardInterrupt:
    # assign: sad face for interrupted input
    #   this handles the case where the user doesn't want to provide input
    #   similar to handling null in the JS version
    reaction = ':('

# --- process input and create reaction ---

else:
    # check: convert input to lower case and compare to 'yes'
    #   checking the user input to validate their response
    #   using .lower() makes the check case-insensitive
    if user_input.lower() == 'yes':
        # assign: the input concatenated with exclamation mark
        #   this is the success path for valid user inputs
        #   we keep their original casing in the response
        reaction = user_input + '!'
    else:
        # assign: baaaad concatenated with the input
        #   this is the path for invalid user inputs (anything but "yes")
        #   shows users what they typed wrong
        reaction = 'baaaaad: ' + user_input

# --- display result to user ---

# call print: show the final reaction
#  all logic is complete, just need to show the reaction to the user
print(reaction)
