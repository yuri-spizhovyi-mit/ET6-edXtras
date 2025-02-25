#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Program for removing either vowels or consonants from text.

This program allows users to enter text and choose whether to remove
all vowels or all consonants from it.

@author: Evan Cole + Claude AI
Adapted from https://github.com/DeNepo/inside-js/tree/main/07-using-functions/
"""

from utils.remove_characters import remove_characters


def get_yes_no(prompt: str) -> bool:
    """Get a yes/no response from the user.

    Args:
        prompt: The question to ask the user.

    Returns:
        bool: True for yes/y, False for no/n.
    """
    while True:
        response = input(prompt).strip().lower()
        if response in ('y', 'yes'):
            return True
        if response in ('n', 'no'):
            return False
        print("Please enter 'y' for yes or 'n' for no.")


def main() -> None:
    """Run the main program loop.
    
    Prompts user for text and whether to remove vowels or consonants,
    then displays the modified result.
    """
    print('Enter some text, then decide if you want to remove the vowels or consonants')
    
    # Get text to modify
    original = input('Enter the text to modify: ').strip()
    while not original:
        original = input('Please enter some text to modify: ').strip()
    
    # Determine what to remove
    remove_vowels = get_yes_no(
        '\nWhat would you like to remove?\n'
        '- Enter y/yes to remove vowels\n'
        '- Enter n/no to remove consonants\n'
    )
    
    removified = ''
    if remove_vowels:
        vowels = 'aeiouAEIOU'
        # Use remove_characters to create a new value with no vowels
        # Initialize this value in removified
        __
    else:
        consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
        # Use remove_characters to create a new value with no consonants
        # Initialize this value in removified
        __
    
    # Display results
    print(f'\nBefore: {original}\nAfter: {removified}')


if __name__ == '__main__':
    main()