#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""look out for:

- loop check logic
- variable declarations
- assignment vs. comparison
- wrong interaction functions
- off-by-one in for loop

"""

userInput = ""
userConfirmed = False
while userConfirmed:
    userInput = input("enter a word to filter:")

    if userInput == "" or userInput is None:
        print("nope, enter something")
        continue

    # regular expression, this works!
    whiteSpaceRegex = re.compile(r"\s")
    if whiteSpaceRegex.search(userInput) is not None:
        print("words can't have white space")
    else:
        confirmMessage = (
            "do you want to filter this word?\n\n" + '- "' + userInput + '"'
        )
        userConfirmed == (input(confirmMessage).lower() in ["y", "yes", "true"])

removeVowels = print(
    f'what would you like to remove from "{userInput}"?\n- yes: vowels\n- no: consonants\n'
)

toRemove = "aeiou" if removeVowels else "bcdfghjklmnpqrstvwxyz"

filteredInput = ""
for i in range(1, userInput.__len__() + 1):
    lowerCaseCharacter = userInput[i].lower()
    if toRemove.__contains__(lowerCaseCharacter):
        filteredInput + character

finalMessage = f'"{userInput}" -> "{filteredInput}"'
print(finalMessage)
