#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
        
    assert isinstance(b, str), "argument is not a string"
    
    c = ""

    for d in b:
        c = d + c

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
