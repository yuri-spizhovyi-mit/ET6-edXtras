#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def reverse(to_reverse: str) -> str:
    """Reverses a string.
    
    Args: 
        str: the string to return

    Returns: The argument, reversed

    Raises:
        AssertionError: if the argument is not a string

    >>> reverse('')
    ''

    >>> reverse('123')
    '321'

    >>> reverse('aabaa')
    'aabaa'
    """

    assert isinstance(to_reverse, str)

    # accumulator variable, storing the reversed string
    #   https://textbooks.cs.ksu.edu/cc310/01-review/10-variable-roles/#accumulator
    backwards = ""

    # one-by-one, append the next character to the front of the reversed string
    for next_character in to_reverse:
        backwards = next_character + backwards

    return backwards


# --- assertion tests ---

assert reverse("") == "", "reverse: Test 0"

assert reverse("Bori") == "iroB", "reverse: Test 1"

assert reverse("<[+]>") == ">]+[<", "reverse: Test 2"

assert reverse("racecar") == "racecar", "reverse: Test 3"

try:
    reverse(123)
except Exception as e:
    pass
else: 
    assert 'did not raise'
