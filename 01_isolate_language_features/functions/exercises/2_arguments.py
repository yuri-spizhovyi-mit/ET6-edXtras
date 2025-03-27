#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Write the function to pass the assertions.
"""


def scramble(param1, param2, param3):
    return param1 + param2 + param3


returned1 = scramble(_, _, _)
assert returned1 == "cab"

returned2 = scramble(_, _, _)
assert returned2 == "abc"

returned3 = scramble(_, _, _)
assert returned3 == "acb"

returned4 = scramble(_, _, _)
assert returned4 == "cba"

returned5 = scramble(_, _, _)
assert returned5 == "cab"

returned6 = scramble(_, _, _)
assert returned6 == "bac"
