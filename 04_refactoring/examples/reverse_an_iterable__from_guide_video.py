#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  =====  describe your function's behavior with a docstring  =====

""" reverses an iterable (string or list)

Arguments:    str | list -> the thing to reverse

Returns:   str | list -> the argument, reversed

Raises:  AssertionError -> when the argument is not an iterable

Examples:

>>> 

>>>

>>>

"""


# ===== import dependencies =====

import traceback


#  =====  write and refactor your solutions  =====


# --- initial solution to refactor ---
def reverse_iterable(iterable: str | list) -> str | list:
    assert isinstance(iterable, (str, list)), "Input must be a string or a list"

    if isinstance(iterable, str):
        return iterable[::-1]
    else:
        return iterable[::-1]


# strategy refactor: simplify redundant logic


def reverse_iterable_cleaned(iterable: str | list) -> str | list:
    assert isinstance(iterable, (str, list)), "Input must be a string or a list"

    return iterable[::-1]


# strategy refactor: use list reverse function - watch out for side-effects!!!


def list_reverse_method(iterable: str | list) -> str | list:
    assert isinstance(iterable, (str, list)), "Input must be a string or a list"

    if isinstance(iterable, list):
        list_copy = iterable.copy()
        list_copy.reverse()
        return list_copy

    return iterable[::-1]


# strategy refactor: split string to list, reverse list (with recursion!), return string


def recursion_string_to_list(iterable: str | list) -> str | list:
    assert isinstance(iterable, (str, list)), "Input must be a string or a list"

    if isinstance(iterable, list):
        list_copy = iterable.copy()
        list_copy.reverse()
        return list_copy

    str_to_list_of_chars = list(iterable)
    reversed_chars = recursion_string_to_list(str_to_list_of_chars)
    return ''.join(reversed_chars)


#  =====  test your solutions  =====


# --- write your function names in this list ---
for solution in [
    reverse_iterable,
    reverse_iterable_cleaned,
    list_reverse_method,
    recursion_string_to_list,
]:
    print("\n>>> ", solution.__name__, "... ", end="")

    try:
        # --- BEGIN assertion tests ---

        assert solution("") == ""
        assert solution([]) == []
        assert solution("9") == "9"
        assert solution([9]) == [9]
        assert solution("19") == "91"
        assert solution([1, 9]) == [9, 1]
        assert solution([19]) == [19]
        # test for side-effects
        list_to_test_for_side_effects = [1, 2, 3]
        assert solution(list_to_test_for_side_effects) == [3, 2, 1]
        assert list_to_test_for_side_effects == [1, 2, 3]

        # --- END assertion tests ---

        print("√")

    except AssertionError:
        print("χ -- test case failure --", "\n")
        traceback.print_exc()

    except Exception as e:
        print("χ -- error --", "\n")
        print("An error occurred:", e)
        traceback.print_exc()

print("\n--- all done ---")
