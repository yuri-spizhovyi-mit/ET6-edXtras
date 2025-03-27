#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""for character of String

iterating through each character in a string is so common
hat there's special syntax to make it easier

"""

userInput = ""
while True:
    userInput = input("enter a word to filter:")

    # -- BEGIN: validate input --

    # -- END: validate input --

removeVowels = input(
    f'what would you like to remove from "{userInput}"?\n- yes: vowels\n- no: consonants\n'
).lower() in ["y", "yes", "true"]

toRemove = ""
if removeVowels:
    toRemove = "AEIOU"
else:
    toRemove = "BCDFGHJKLMNPQRSTVWXYZ"

filteredInput = ""
# -- BEGIN: filter input --

# -- END: filter input --

finalMessage = f'"{userInput}" -> "{filteredInput}"'

print(finalMessage)
