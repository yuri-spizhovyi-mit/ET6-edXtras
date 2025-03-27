#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  =====  describe your function's behavior with a docstring  =====

"""Repeats a string a specific number of times.

Arguments:
    string - the text to repeat, defaults to an empty string
    int - the number of times to repeat the text. defaults to 0

Returns: string - containing the argument repeated n times.

Raises:
    AssertionError - the first argument is not a string
    AssertionError - the second argument is not an integer
    AssertionError - the second argument is less than 0

Examples:

>>> repeat_a_string('a', 0)
''

>>> repeat_a_string('', 4)
''

>>> repeat_a_string('ab', 3)
'ababab'

"""


# ===== import dependencies =====

import traceback


#  =====  write and refactor your solutions  =====


# --- initial solution to refactor ---
#  can be from you, LeetCode, stackoverflow, a peer, an LLM, ...
def repeat_a_string(to_repeat: str = "", repetitions: int = 0) -> str:
    assert isinstance(to_repeat, str), "first argument must be a string"
    assert isinstance(repetitions, int), "second argument must be an integer"
    assert repetitions >= 0, "second argument is less than 0"

    repeated = ""
    for _ in range(repetitions):
        repeated += to_repeat

    return repeated


# implementation refactor - try with more fun variable names


def repeat_a_string_storylike(repeat_me: str = "", this_many_times: int = 0) -> str:
    assert isinstance(repeat_me, str), "first argument must be a string"
    assert isinstance(this_many_times, int), "second argument must be an integer"
    assert this_many_times >= 0, "second argument is less than 0"

    repeat_merepeat_me = ""
    for repetition in range(this_many_times):
        repeat_merepeat_me += repeat_me

    return repeat_merepeat_me


# strategy refactor, take advantage of python operators - multiply string by repetitions


def multiply_string_by_repetitions(to_repeat: str = "", repetitions: int = 0) -> str:
    assert isinstance(to_repeat, str), "first argument must be a string"
    assert isinstance(repetitions, int), "second argument must be an integer"
    assert repetitions >= 0, "second argument is less than 0"

    return to_repeat * repetitions


# implementation refactor, use more storylike variable names


def multiply_string_by_repetitions_storylike(
    repeat_me: str = "", this_many_times: int = 0
) -> str:
    assert isinstance(repeat_me, str), "first argument must be a string"
    assert isinstance(this_many_times, int), "second argument must be an integer"
    assert this_many_times >= 0, "second argument is less than 0"

    return repeat_me * this_many_times


# strategy refactor - iterate with while loop until the string is long enough


def iterate_until_length_is_correct(text: str = "", repeats: int = 0) -> str:
    assert isinstance(text, str), "first argument must be a string"
    assert isinstance(repeats, int), "second argument must be an integer"
    assert repeats >= 0, "second argument is less than 0"

    accumulator = ""
    while len(accumulator) != (len(text) * repeats):
        accumulator += text

    return accumulator


# implementation refactor - use an extra variable to make the length more clear


def iterate_until_length_is_correct__readabiilty(
    text: str = "", repeats: int = 0
) -> str:
    assert isinstance(text, str), "first argument must be a string"
    assert isinstance(repeats, int), "second argument must be an integer"
    assert repeats >= 0, "second argument is less than 0"

    solution_length = len(text) * repeats

    accumulator = ""
    while len(accumulator) != solution_length:
        accumulator += text

    return accumulator


# implementation refactor - checking for < instead of != better communicates the strategy


def iterate_until_length_is_correct__readabiilty_2(
    text: str = "", repeats: int = 0
) -> str:
    assert isinstance(text, str), "first argument must be a string"
    assert isinstance(repeats, int), "second argument must be an integer"
    assert repeats >= 0, "second argument is less than 0"

    solution_length = len(text) * repeats

    accumulator = ""
    while len(accumulator) < solution_length:
        accumulator += text

    return accumulator


# strategy refactor - recursion, starting with the template. base case: 0 repeats


def recursion_base_case_repeats_template(text: str = "", repeats: int = 0) -> str:
    assert isinstance(text, str), "first argument must be a string"
    assert isinstance(repeats, int), "second argument must be an integer"
    assert repeats >= 0, "second argument is less than 0"

    base_case = repeats == 0  # must use argument
    if base_case:
        turn_around = ""
        return turn_around

    break_down = repeats - 1  # must use argument
    recursion = recursion_base_case_repeats_template(text, break_down)
    build_up = recursion + text  # must use recursion

    return build_up


# implementation refactor - clear out the template


def recursion_base_case_repeats(text: str = "", repeats: int = 0) -> str:
    assert isinstance(text, str), "first argument must be a string"
    assert isinstance(repeats, int), "second argument must be an integer"
    assert repeats >= 0, "second argument is less than 0"

    if repeats == 0:
        return ""

    return recursion_base_case_repeats(text, repeats - 1) + text


# implementation refactor - make it a tailcall recursion


def recursion_base_case_repeats_tailcall(text: str = "", repeats: int = 0) -> str:
    assert isinstance(text, str), "first argument must be a string"
    assert isinstance(repeats, int), "second argument must be an integer"
    assert repeats >= 0, "second argument is less than 0"

    if repeats == 0:
        return ""

    return text + recursion_base_case_repeats_tailcall(text, repeats - 1)


# strategy refactor - add memoization.
# also a backwards-compatible behavior refactorL:
#   it changes the function's signature without breaking previous test cases


def recursion_base_case_repeats_memo(
    text: str = "", repeats: int = 0, cache: dict = {}
) -> str:
    assert isinstance(text, str), "first argument must be a string"
    assert isinstance(repeats, int), "second argument must be an integer"
    assert repeats >= 0, "second argument is less than 0"

    key = f"{repeats}{text}"
    if key in cache:
        return cache[key]

    if repeats == 0:
        return ""

    result = text + recursion_base_case_repeats_memo(text, repeats - 1, cache)
    cache[key] = result
    return result


# strategy & implementation refactor - make a storylike implementation with memoization


def storylike_with_memo(
    the_input: str = "", this_many_times: int = 0, the_past: dict = {}
) -> str:
    """Those who cannot remember the past are doomed to repeat it."""

    assert isinstance(the_input, str), "first argument must be a string"
    assert isinstance(this_many_times, int), "second argument must be an integer"
    assert this_many_times >= 0, "second argument is less than 0"

    task = f"I am to repeat '{the_input} {this_many_times}'."

    if task in the_past:
        return the_past[task]

    the_current_task = the_input * this_many_times

    the_past[task] = the_current_task

    return the_current_task


#  =====  test your solutions  =====


# --- write your function names in this list ---
for solution in [
    repeat_a_string,
    repeat_a_string_storylike,
    multiply_string_by_repetitions,
    multiply_string_by_repetitions_storylike,
    iterate_until_length_is_correct,
    iterate_until_length_is_correct__readabiilty,
    iterate_until_length_is_correct__readabiilty_2,
    recursion_base_case_repeats_template,
    recursion_base_case_repeats,
    recursion_base_case_repeats_tailcall,
    recursion_base_case_repeats_memo,
    storylike_with_memo,
]:
    print("\n>>> ", solution.__name__, "... ", end="")

    try:
        # --- BEGIN assertion tests ---

        assert solution() == ""
        assert solution("") == ""
        assert solution("", 0) == ""
        assert solution("", 30) == ""
        assert solution("a", 0) == ""
        assert solution("a", 1) == "a"
        assert solution("a", 2) == "aa"
        assert solution("aa", 1) == "aa"
        assert solution("aba", 1) == "aba"
        assert solution("aba", 3) == "abaabaaba"
        assert solution("<{+}>", 7) == "<{+}><{+}><{+}><{+}><{+}><{+}><{+}>"
        assert (
            solution('"Go!", said Dr. Seuss?', 2)
            == '"Go!", said Dr. Seuss?"Go!", said Dr. Seuss?'
        )

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
