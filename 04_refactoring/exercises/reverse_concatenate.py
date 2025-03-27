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
def reverse_concatenate(array_of_strings: list[str]) -> str:
    assert isinstance(array_of_strings, list), "argument is not a list"
    assert all(isinstance(item, str) for item in array_of_strings), (
        "argument contains non-strings"
    )

    reversed_array = array_of_strings[::-1]
    return "".join(reversed_array)


#  =====  test your solutions  =====


# --- write your function names in this list ---
for solution in [reverse_concatenate]:
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
