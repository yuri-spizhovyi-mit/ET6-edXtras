#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" and & or
  short circuiting!  don't forget it
  it's possible to get the same result different ways
  hint: if you highlight a line, only that line will be traced
"""

# --- booleans ---

assert  (True or (False and True)) == _, 'a'

assert ((True or False) and True) == _, 'b'

assert (True and (False or False) and True) == _, 'c'

assert (True or (False and False) or True) == _, 'd'

assert ((True or False) and (False or True)) == _, 'e'


# --- numbers ---

assert (1 or (0 and 2)) == _, 'f'

assert ((1 or 0) and 2) == _, 'g'

assert (1 and (0 or 0) and 2) == _, 'h'

assert (1 or (0 and 0) or 2) == _, 'i'

assert ((1 or 0) and (0 or 2)) == _, 'j'


# --- strings ---

assert ('hi' or ('' and 'bye')) == _, 'k'

assert (('hi' or '') and 'bye') == _, 'l'

assert ('hi' and ('' or '') and 'bye') == _, 'm'

assert ('hi' or ('' and '') or 'bye') == _, 'n'

assert (('hi' or '') and ('' or 'bye')) == _, 'o'
