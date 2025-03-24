#!/usr/bin/env python3
# -*- coding: utf-8 -*-

userInput = ""

inputIsAboutFrogs = _
while not inputIsAboutFrogs:
    userInput = input("tell me something about frogs")
    print("userInput:", type(userInput), userInput)

    # check if the user entered nothing, or clicked cancel
    if _:
        print("that is not something")
        continue

    # search the user input for "frog", upper or lower case
    if _:
        inputIsAboutFrogs = _
        continue

    print("nope, not about frogs.  try again.")

finalMessage = 'i just learned something cool about frogs!\n\n- "' + userInput + '"'

print(finalMessage)
