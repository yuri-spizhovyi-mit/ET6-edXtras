#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  =====  describe your function's behavior with a docstring  =====

"""

Arguments:

Returns:

Raises:

Examples:

>>>

>>>

>>>

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
for solution in []:
    print("\n>>> ", solution.__name__, "... ", end="")

    try:
        # --- BEGIN assertion tests ---

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
