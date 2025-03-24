#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module for demonstrating character code manipulation.

This program shows how to shift characters by their Unicode values.
Contains code sections marked for refactoring into a separate utility function.

@author: Evan Cole + Claude AI
Adapted from https://github.com/DeNepo/inside-js/tree/main/07-using-functions/s
"""
from typing import Optional


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

    Raises:
        ValueError: If validator is provided and input fails validation
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


def get_number_input(prompt: str) -> int:
    """Get and validate numeric input from user.

    Args:
        prompt: The message to show when requesting input

    Returns:
        int: The validated numeric input
    """
    while True:
        try:
            return int(get_validated_input(prompt))
        except ValueError:
            print("Please enter a valid number")


def main() -> None:
    """Run the main program loop.
    
    Prompts user for text and shift value, then demonstrates
    character code manipulation with code marked for refactoring.
    """
    # Get validated inputs
    while True:
        user_input = get_validated_input(
            'Enter a phrase, each character will be shifted by character code: '
        )
        unicode_shift = get_number_input(
            'How many unicode numbers do you want the characters to shift? '
        )
        
        # Confirm inputs
        confirm_message = f'Is this correct?\n\n- "{user_input}"\n- {unicode_shift}'
        if input(confirm_message + ' (y/n): ').lower().startswith('y'):
            break
    
    # BEGIN: refactor to use `shift_characters`
    encoded_string = ''
    for character in user_input:
        character_code = ord(character)
        new_char_code = character_code + unicode_shift
        encoded_character = chr(new_char_code)
        encoded_string += encoded_character
    # END: refactor
    
    print(f'"{user_input}" -> "{encoded_string}"')


if __name__ == '__main__':
    main()
