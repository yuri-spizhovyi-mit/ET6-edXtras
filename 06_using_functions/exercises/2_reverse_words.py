#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A program that reverses each word a user's input.

@author: Evan Cole
"""

from utils.reverse_string import reverse_string

user_phrase = input("Enter a phrase, I will reverse each word. \n:  ")

user_words = user_phrase.split(" ")

reversed_words = [reverse_string(word) for word in user_words]

reversed_phrase = " ".join(reversed_words)

print(f"-> {reversed_phrase}")
