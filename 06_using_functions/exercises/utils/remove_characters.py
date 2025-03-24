#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module for string character removal operations.

This module provides functionality for removing specified characters from strings
while preserving case sensitivity and handling empty inputs appropriately.

@author: Evan Cole + Claude AI
Adapted from https://github.com/DeNepo/inside-js/tree/main/07-using-functions/
"""

from typing import Optional


def remove_characters(text: Optional[str] = None, to_remove: Optional[str] = None) -> str:
    """Remove all specified characters from the input text.

    Args:
        text: The input string to remove characters from. Defaults to empty string
            if None is provided. Must be a string if provided.
        to_remove: The characters to remove from the text. Defaults to empty string
            if None is provided. Must be a string if provided.

    Returns:
        str: A new string with all specified characters removed.

    Raises:
        TypeError: If text or to_remove are provided but are not strings.


    >>> remove_characters('hello', 'l')
    'heo'
    >>> remove_characters('hello', 'L')
    'hello'
    >>> remove_characters('hello', 'ho')
    'ell'
    >>> remove_characters()
    ''
    """
    # Handle default parameters
    if text is None:
        text = ''
    if to_remove is None:
        to_remove = ''
    
    # Add defensive assertions
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(to_remove, str):
        raise TypeError("to_remove must be a string")

    # Remove each character sequentially
    result = text
    for char in to_remove:
        result = result.replace(char, '')
    
    return result