#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Test module for remove_characters function.

This module contains comprehensive tests for the remove_characters function,
verifying its behavior with various inputs and edge cases.

@author: Evan Cole + Claude AI
Adapted from https://github.com/DeNepo/inside-js/tree/main/07-using-functions/
"""

import unittest
from ..remove_characters import remove_characters


class TestRemoveCharacters(unittest.TestCase):
    """Test suite for the remove_characters function.
    
    Tests cover basic functionality, edge cases, and error handling for the
    remove_characters function.
    """

    def test_basic_character_removal(self):
        """Verify basic character removal functionality."""
        self.assertEqual(remove_characters('hello', 'l'), 'heo')

    def test_removes_all_characters(self):
        """Verify that all characters can be removed from a string."""
        self.assertEqual(remove_characters('asdf', 'fsda'), '')

    def test_case_sensitive_removal(self):
        """Verify that character removal is case-sensitive."""
        self.assertEqual(remove_characters('asdf', 'ASDF'), 'asdf')

    def test_removes_adjacent_characters(self):
        """Verify that adjacent characters are properly removed."""
        self.assertEqual(remove_characters('asdf', 'as'), 'df')

    def test_removes_non_adjacent_characters(self):
        """Verify that non-adjacent characters are properly removed."""
        self.assertEqual(remove_characters('asdf', 'ad'), 'sf')

    def test_removes_repeated_characters(self):
        """Verify handling of repeated characters in input."""
        self.assertEqual(remove_characters('hello there', 'e'), 'hllo thr')

    def test_removes_repeated_removal_chars(self):
        """Verify handling of repeated characters in removal string."""
        self.assertEqual(remove_characters('hello', 'll'), 'heo')


class TestEdgeCases(unittest.TestCase):
    """Test suite for edge cases and boundary conditions.
    
    Tests various edge cases including empty strings, spaces, and special characters.
    """

    def test_empty_input_string(self):
        """Verify behavior with empty input string."""
        self.assertEqual(remove_characters('', 'asdf'), '')

    def test_empty_removal_string(self):
        """Verify behavior with empty removal string."""
        self.assertEqual(remove_characters('asdf', ''), 'asdf')

    def test_space_handling(self):
        """Verify proper handling of spaces."""
        self.assertEqual(remove_characters('a b c', ' '), 'abc')

    def test_special_characters(self):
        """Verify handling of special characters."""
        self.assertEqual(remove_characters('a\nb\tc', '\n\t'), 'abc')

    def test_unicode_characters(self):
        """Verify handling of unicode characters."""
        self.assertEqual(remove_characters('héllö', 'ö'), 'héll')


class TestDefaultParameters(unittest.TestCase):
    """Test suite for default parameter behavior.
    
    Tests the function's behavior when parameters are omitted or None.
    """

    def test_default_second_parameter(self):
        """Verify behavior when only first parameter is provided."""
        self.assertEqual(remove_characters('asdf'), 'asdf')

    def test_default_both_parameters(self):
        """Verify behavior when no parameters are provided."""
        self.assertEqual(remove_characters(), '')

    def test_none_first_parameter(self):
        """Verify handling of None as first parameter."""
        self.assertEqual(remove_characters(None, 'a'), '')

    def test_none_second_parameter(self):
        """Verify handling of None as second parameter."""
        self.assertEqual(remove_characters('asdf', None), 'asdf')

    def test_both_none_parameters(self):
        """Verify handling when both parameters are None."""
        self.assertEqual(remove_characters(None, None), '')


class TestDefensiveChecks(unittest.TestCase):
    """Test suite for defensive programming checks.
    
    Tests the function's error handling for invalid inputs.
    """

    def test_non_string_text(self):
        """Verify TypeError is raised for non-string text parameter."""
        with self.assertRaises(TypeError):
            remove_characters(123, 'a')

    def test_non_string_to_remove(self):
        """Verify TypeError is raised for non-string to_remove parameter."""
        with self.assertRaises(TypeError):
            remove_characters('asdf', 123)

    def test_non_string_both_parameters(self):
        """Verify TypeError is raised when both parameters are non-strings."""
        with self.assertRaises(TypeError):
            remove_characters(123, 456)
