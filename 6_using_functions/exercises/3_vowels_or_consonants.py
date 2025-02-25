#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module for demonstrating character filtering in strings.

This program shows how to iterate through characters in a string and filter them
based on user-specified criteria. Contains code sections marked for refactoring
into a separate utility function.

@author: Evan Cole + Claude AI
Adapted from https://github.com/DeNepo/inside-js/tree/main/07-using-functions/s
"""

from typing import Optional
import re


def get_validated_input(prompt: str, 
                       error_msg: str = "Please enter something", 
                       validator: Optional[callable] = None) -> str:
    """Get and validate user input.

    Args:
        prompt: The message to show when requesting input
        error_msg: Message to show if validation fails
        validator: Optional function to validate input

    Returns:
        str: The validated user input
    """
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print(error_msg)
            continue
        if validator and not validator(user_input):
            print(error_msg)
            continue
        return user_input


def main() -> None:
    """Run the main program loop.
    
    Prompts user for text and filtering preferences, then demonstrates
    character filtering with code marked for refactoring.
    """
    # Get and validate user input
    while True:
        user_input = get_validated_input(
            'Enter a word to filter: ',
            "Words can't have white space",
            lambda x: not re.search(r'\s', x)
        )
        
        confirm_message = f'Do you want to filter this word?\n\n- "{user_input}"'
        if input(confirm_message + ' (y/n): ').lower().startswith('y'):
            break
    
    # Determine what to remove
    remove_vowels = input(
        f'What would you like to remove from "{user_input}"?\n'
        '- Enter y for vowels, n for consonants: '
    ).lower().startswith('y')
    
    to_remove = 'aeiou' if remove_vowels else 'bcdfghjklmnpqrstvwxyz'
    
    # BEGIN: refactor this to call `filter`
    filtered_input = ''
    for character in user_input:
        lower_case_character = character.lower()
        if not to_remove.__contains__(lower_case_character):
            filtered_input += character
    # END: refactor
    
    print(f'"{user_input}" -> "{filtered_input}"')


if __name__ == '__main__':
    main()