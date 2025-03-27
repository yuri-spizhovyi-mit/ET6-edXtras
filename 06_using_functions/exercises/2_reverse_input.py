#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A program that reverses a user's entire input.

@author: Evan Cole
"""

from utils.reverse_string import reverse_string

user_phrase = input("Enter a phrase, I will reverse it. \n:  ")

backwards_phrase = reverse_string(user_phrase)

print(f"-> {backwards_phrase}")
