#!/usr/bin/env python3
# -*- coding: utf-8 -*-


""" everything mixed together
    these expressions are strange things to practice tracing
    you won't come across things like this too often
    and you shouldn't be writing them either!
"""

w = 'HELLO'
x = True
y = 4
z = -4

# ---

assert  (type(type(x).__name__) == type(w)) == _, 'a'

assert (len(w) >= y + 1) == _, 'b'

assert  (y + z == w[4]) == _, 'c'

assert (y + z or x) == _, 'd'

assert  (x == (len(w[1:5]) == y)) == _, 'e'
