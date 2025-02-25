#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# - decalare a function with one argument that takes and returns a string
def reverse_string(to_reverse: str) -> str:
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
        
    # make sure the developer passed in the correct type
    # - assert that that the argument is type string
    assert isinstance(to_reverse, str), "argument is not a string"
    
    # accumulator variable, storing the reversed string
    #   https://textbooks.cs.ksu.edu/cc310/01-review/10-variable-roles/#accumulator
    # - declare variable c storing an empty string
    reversed_input = ""

    # one-by-one, append the next character to the front of the reversed string
    #  - iterate over each character in the argument
    for next_character in to_reverse:
        # - concatenate the values in d and c, assign them to c
        reversed_input = next_character + reversed_input

    # - return the value stored in c
    return reversed_input

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
