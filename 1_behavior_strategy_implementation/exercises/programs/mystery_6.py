#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" """

sentence = ""

while True:
    sentence = input("Enter a sentence with at least 2 words: ")
    if sentence is None:
        print("There is no escape")
    elif len(sentence) < 3:
        print(f'"{sentence}" is too short to have two words')
    elif " " not in sentence:
        print("There is no space")
    else:
        break

words = sentence.split()
new_sentence = []

for word in words:
    keep = input(f"Do you want to keep this word? (yes/no): {word}\n").strip().lower()
    if keep == "yes":
        new_sentence.append(word)

print(" ".join(new_sentence))
