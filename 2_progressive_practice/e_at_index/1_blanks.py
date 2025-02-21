#!/usr/bin/env python3
# -*- coding: utf-8 -*-

validInput = ''

index = 0
while validInput == '':
    index = _ + 1

    userInput = input(
        f'enter anything with "e" or "E" as the {index}th letter:\n>>> '
    )

    if userInput is None or userInput == '':
        print('that is nothing')
    elif _(userInput) < _:
        print('too short')
    elif userInput[_] == 'e' or userInput[_] == 'E':
        _ = userInput
    else:
        print(_)

print('done: "' + validInput + '"')
