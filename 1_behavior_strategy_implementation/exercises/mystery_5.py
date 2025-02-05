#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" """

# --- declare function ---


def a(b: list) -> list:
    """Creates a reversed copy of a list"""
    c = []
    for item in b:
        c.insert(0, item)
    return c


# --- test function ---


assert a([]) == [], "Test 0"

assert  a(["x", "y", "z"]) == ["z", "y", "x"], "Test 1"

assert  a( [True, False]) == [False, True], "Test 2"

assert  a( [1729]) == [1729], "Test 3"

d = [1, 2, 3]
a(d)
assert d == [1, 2, 3], "Test 4"
