#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" """

a = ""
while a == "":
    a = input("Enter some text to reverse: ")
    if a == "":
        print("nope, you have to enter something")

b = ""
for c in a:
    b = c + b

print("here is your reversed input: " + b)
