#!/usr/bin/env python3
# -*- coding: utf-8 -*-


try:
    a = input('enter the word "yes", upper or lower case: ')
except KeyboardInterrupt:
    b = ':('
else:
    if a.lower() == 'yes':
        b = a + '!'
    else:
        b = 'baaaaad: ' + a

print(b)
