#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" """

# --- declare the helper function ---


def a(b: str) -> str:
    """ """
    c = ""
    for d in b:
        c = d + c
    return c

assert a("") == "", "Test 0"
assert a("xyz") == "zyx", "Test 1"
assert a("Malayalam") == "malayalaM", "Test 2"
assert a("1729") == "9271", "Test 3"


# --- use the helper function in a program ---


e = ""
while e == "":
    e = input("\nEnter some something to reverse: ")
    if e == "":
        print("Nope, gotta enter something.  Try again.")

f = a(e)

print(e, " -> ", f)
