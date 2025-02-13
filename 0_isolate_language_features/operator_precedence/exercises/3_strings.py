#!/usr/bin/env python3
# -*- coding: utf-8 -*-


w = 'potato'
x = 'long tea'
y = 'horse'
z = 'jar'

# ---

assert (type(w) == type(y)) == _, 'a'

assert (y + ' ' + z == 'horsejar') == _, 'b'

assert (x.__len__() < 4 or 10 < x.__len__()) == _, 'c'

assert (4 < x.__len__() or x.__len__() < 10) == _, 'd'

assert (z[2] == y[2] and len(z) < len(y)) == _, 'e'

assert  (len(w) >= 6 and 'to' in w) == _, 'f'
