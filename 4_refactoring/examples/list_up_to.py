#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  =====  describe your function's behavior with a docstring  =====

""" Generates a list with the integers from 0 -> n, in order.

Arguments: n, integer - the highest number in the list. defaults to 0.

Returns: list - all the integers from 0 -> n in order.

Raises: 
    AssertionError if the argument is not an integer
    AssertionError if the argument is less than 0

Examples:

>>> list_up_to(0)
[0]

>>> list_up_to(3)
[0, 1, 2, 3]

>>> list_up_to(7)
[0, 1, 2, 3, 4, 5, 6, 7]

"""


# ===== import dependencies =====

import traceback


#  =====  write and refactor your solutions  =====


def append_list_length_until_length__a(n: int = 0) -> list:
    assert isinstance(n, int), "n must be an integer"
    assert n >= 0, "n must be greater than or equal to 0"

    numbers = []
    # append the current length of the list until the list is long enough
    while len(numbers) <= n:
        numbers.append(len(numbers))
    return numbers


# That's an ok solution, but the long line in the while loop is a little dense.
#  Let's try a small implementation refactor using a variable to help understand the strategy


def append_list_length_until_length__b(n: int = 0) -> list:
    assert isinstance(n, int), "n must be an integer"
    assert n >= 0, "n must be greater than or equal to 0"

    numbers = []
    # append the current length of the list until the list is long enough
    while len(numbers) <= n:
        next_number = len(numbers)
        numbers.append(next_number)
    return numbers


# Great! The code still passes the same tests (has the same behavior) and is easier to understand,
# but I'm still curious if I can't make this easier to understand.
# Let's make a minor strategy refactor to iterate until last item in our list is n:


def append_list_length_until_n(n: int = 0) -> list:
    assert isinstance(n, int), "n must be an integer"
    assert n >= 0, "n must be greater than or equal to 0"

    numbers = [0]
    # append the current length of the list until the last item is n
    while numbers[-1] != n:
        next_number = len(numbers)
        numbers.append(next_number)
    return numbers


# Hold on, maybe a for loop would be more clear.
# They're meant for iterating over a range, and then I wouldn't need an extra line to declare my stepper variable


def for_iterator(n: int = 0) -> list:
    numbers = []
    # iterate from 0 to n, appending each number as you go
    for next_int in range(n + 1):
        numbers.append(next_int)
    return numbers


# That's enough iteration. Let's try with recursion, starting from the template function


def reacursion_template(n: int = 0) -> list:
    assert isinstance(n, int), "n must be an integer"
    assert n >= 0, "n must be greater than or equal to 0"

    base_case = n == 0  # must use argument
    if base_case:
        turn_around = [0]
        return turn_around

    break_down = n - 1  # must use argument
    recursion = reacursion_template(break_down)
    build_up = recursion + [n]  # must use recursion

    return build_up


# That template was helpful for creating my recursive solution,
# but now that I understand what I'm doing it's a lot of code to read.
# Let's simply this recursive function:


def recursion_concatenate(n: int = 0) -> list:
    assert isinstance(n, int), "n must be an integer"
    assert n >= 0, "n must be greater than or equal to 0"

    if n == 0:
        return [0]

    return recursion_concatenate(n - 1) + [n]


# strategy refactor, modifying the list in place instead of creating a new one


def recursion_append(n: int = 0) -> list:
    assert isinstance(n, int), "n must be an integer"
    assert n >= 0, "n must be greater than or equal to 0"

    if n == 0:
        return [0]

    result = recursion_append(n - 1)
    result.append(n)
    return result


# strategy refactor - use list comprehension

def list_comprehension(max: int = 0) -> list:
    assert isinstance(max, int), "input must be an integer"
    assert max >= 0, "input must be greater than or equal to 0"

    return [i for i in range(max + 1)]


#  =====  test your solutions  =====


# --- write your function names in this list ---
for solution in [
    append_list_length_until_length__a,
    append_list_length_until_length__b,
    append_list_length_until_n,
    for_iterator,
    reacursion_template,
    recursion_concatenate,
    recursion_append,
    list_comprehension,
]:
    print(f"\n{solution.__name__} ... ", end="")

    try:
        # ---BEGIN assertion tests ---

        assert solution(0) == [0]
        assert solution(2) == [0, 1, 2]
        assert solution(6) == [0, 1, 2, 3, 4, 5, 6]
        assert solution(9) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert solution(13) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        # ---END assertion tests ---

        print("√")

    except AssertionError:
        print("χ -- test case failure --", "\n")
        traceback.print_exc()

    except Exception as e:
        print("χ -- error --", "\n")
        print("An error occurred:", e)
        traceback.print_exc()

print("\n--- all done ---")
