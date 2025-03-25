#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  =====  describe your function's behavior with a docstring  =====

""" Repeats a string a specific number of times.

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


#  =====  test your solutions  =====


# --- write your function names in this list ---
for solution in [repeat_a_string]:
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
