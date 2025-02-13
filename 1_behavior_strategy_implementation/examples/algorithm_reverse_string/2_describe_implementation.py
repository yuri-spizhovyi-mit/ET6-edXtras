#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# - decalare a function with one argument that takes and returns a string
def a(b: str) -> str:
    """Reverses a string.
    
    Args: 
        str: the string to return

    Returns: The argument, reversed

    Raises:
        AssertionError: if the argument is not a string

    >>> a('')
    ''

    >>> a('123')
    '321'

    >>> a('aabaa')
    'aabaa'
    """
        
    # - assert that that the argument is type string
    assert isinstance(b, str), "argument is not a string"
    
    # - declare variable c storing an empty string
    c = ""

    #  - iterate over each character in the argument
    for d in b:
        # - concatenate the values in d and c, assign them to c
        c = d + c

    # - return the value stored in c
    return c

# --- assertion tests ---

assert a("") == "", "Test 0"

assert a("Bori") == "iroB", "Test 1"

assert a("<[+]>") == ">]+[<", "Test 2"

assert a("racecar") == "racecar", "Test 3"

try:
    a(123)
except Exception as e:
    pass
else: 
    assert 'did not raise'
