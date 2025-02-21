#!/usr/bin/env python3
# -*- coding: utf-8 -*-

validInput = ''

index = 0
isValid = False
while not isValid:
    index = index + 1

    userInput = input(
        f'enter anything with "e" or "E" as the {index}th letter:\n>>> '
    )

    # -- BEGIN: validate input --
    
    # -- END: validate input --

print('done: "' + validInput + '"')
