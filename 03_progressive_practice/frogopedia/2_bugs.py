#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""look out for:

- logical operators
- boolean flag values

"""

userInput = ""
inputIsAboutFrogs = True
while not inputIsAboutFrogs:
    userInput = input("tell me something about frogs")

    if inputIsAboutFrogs == "" and inputIsAboutFrogs is None:
        print("that is not something")
    # regular expression: this works!
    elif re.search(r"frog", userInput, re.IGNORECASE) is not None:
        inputIsAboutFrogs = False
    else:
        print("nope, not about frogs.  try again.")

finalMessage = 'i just learned something cool about frogs!\n\n- "' + userInput + '"'
print(finalMessage)
