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
def count_down(start: int = 0) -> list[int]:
    assert isinstance(start, int), "argument is not an integer"
    assert start >= 0, "argument is less than 0"

    result = []
    for i in range(start, -1, -1):
        result.append(i)
    return result


#  =====  test your solutions  =====


# --- write your function names in this list ---
for solution in [count_down]:
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
