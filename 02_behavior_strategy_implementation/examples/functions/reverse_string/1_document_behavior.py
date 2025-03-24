#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def reverse_string(b: str) -> str:
    """Reverses a string.
    
    Args: 
        str: the string to return

    Returns: The argument, reversed

    Raises:
        AssertionError: if the argument is not a string

    >>> reverse_string('')
    ''

    >>> reverse_string('123')
    '321'

    >>> reverse_string('aabaa')
    'aabaa'
    """
        
    assert isinstance(b, str), "argument is not a string"
    
    c = ""

    for d in b:
        c = d + c

    return c

# --- assertion tests ---

assert reverse_string("") == "", "Test 0"

assert reverse_string("Bori") == "iroB", "Test 1"

assert reverse_string("<[+]>") == ">]+[<", "Test 2"

assert reverse_string("racecar") == "racecar", "Test 3"

try:
    reverse_string(123)
except Exception as e:
    pass
else: 
    assert 'did not raise'
