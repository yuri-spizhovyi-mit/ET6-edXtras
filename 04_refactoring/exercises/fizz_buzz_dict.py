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
def fizz_buzz_dict(max_num: int) -> dict[int, str | int]:
    assert isinstance(max_num, int), "max is not an integer"
    assert max_num >= 0, "max is less than 0"

    result = {}
    for i in range(max_num):
        if i % 3 == 0 and i % 5 == 0:
            result[i] = "fizzbuzz"
        elif i % 3 == 0:
            result[i] = "fizz"
        elif i % 5 == 0:
            result[i] = "buzz"
        else:
            result[i] = i
    return result


#  =====  test your solutions  =====


# --- write your function names in this list ---
for solution in [fizz_buzz_dict]:
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
