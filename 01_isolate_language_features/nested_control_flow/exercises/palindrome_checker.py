#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Checking for a Palindrome

A palindrome reads the same forward and backward.
Use a loop to check if a word is a palindrome.
"""

word = input("enter a word, find out if it is a palindrome: ")

is_palindrome = True

for _ in range(_):  # loop over half the word
    if word[_]._() != word[_]._():  # comparison should be case-insensitive
        is_palindrome = False
        break

print("yes" if is_palindrome else "no")

# challenge: refactor this so it works for phrases with spaces
