#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Write the function to pass the assertions.
'''

def scramble(param1, param2, param3):
    return param3 + param1 + param2

_1_actual = scramble('x', 'z', 'y')
_1_expect = 'yxz'
assert _1_actual == _1_expect

_2_actual = scramble('x', 'y', 'z')
_2_expect = 'zxy'
assert _2_actual == _2_expect

_3_actual = scramble('z', 'x', 'y')
_3_expect = 'yzx'
assert _3_actual == _3_expect
