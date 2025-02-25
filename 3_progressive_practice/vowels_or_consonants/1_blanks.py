#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

"""for character of String

  iterating through each character in a string is so common
  that there's special syntax to make it easier

"""

userInput = ""
userConfirmed = False
while _:
    userInput = input("enter a word to filter:")

    if userInput == "" or userInput is None:
        print("nope, enter something")
        continue

    whiteSpaceRegex = re.compile(r"\s")
    if whiteSpaceRegex._(userInput):
        print("words can't have white space")
        continue

    confirmMessage = "do you want to filter this word?\n\n" + '- "' + userInput + '"'
    _ = input(confirmMessage).lower() in ["y", "yes", "true"]

removeVowels = input(
    f'what would you like to remove from "{_}"?\n- yes: vowels\n- no: consonants\n'
).lower() in ["y", "yes", "true"]

toRemove = "_" if removeVowels else "_"

filteredInput = ""
for character in userInput:
    lowerCaseCharacter = character.lower()
    if _:
        _

finalMessage = f'"{userInput}" -> "{filteredInput}"'

print(finalMessage)
