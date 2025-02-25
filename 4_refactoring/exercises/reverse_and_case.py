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
def reverse_as_case(text: str = "", lower_case: bool = True) -> str:
    assert isinstance(text, str), "first argument is not a string"
    assert isinstance(lower_case, bool), "second argument is not a boolean"

    reversed_text = text[::-1]

    if lower_case:
        return reversed_text.lower()
    else:
        return reversed_text.upper()


#  =====  test your solutions  =====


# --- write your function names in this list ---
for solution in [reverse_as_case]:
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
