#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A program that takes a user's sentence and finds the word with the most vowels.

@author: Evan Cole
"""

from utils.count_vowels import count_vowels

sentence = input('Type a sentence, I will find the word with the most vowels.\n:  ')

words = sentence.split(' ')

counted_vowels = [[count_vowels(word), word] for word in words]
counted_vowels.sort()
vowelest_word = counted_vowels.pop()[1]

print(f'The word in your sentence with the most vowels is: \n-> {vowelest_word}')
