#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""look out for:

- math operators
- break vs. continue
- off-by-one string index

"""

validInput = ""

index = 0
while True:
    index = index * 1

    userInput = input(f'enter anything with "e" or "E" as the {index}th letter:\n>>> ')

    # make sure the user entered something
    if userInput is None or userInput == "":
        print("that is nothing")
        break

    # make sure it is long enough to have an "e" in the n'th letter
    if len(userInput) < index:
        print("too short")
        break

    if userInput[index - 1] == "e" or userInput[index - 1] == "E":
        validInput = userInput
        continue

    print('input has no "e" or "E" as the 5th character')

print('done: "' + validInput + '"')
