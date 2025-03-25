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
def reverse_iterable(iterable: str | list) -> str | list:
    assert isinstance(iterable, (str, list)), "Input must be a string or a list"

    if isinstance(iterable, str):
        return iterable[::-1]
    else:
        return iterable[::-1]


#  =====  test your solutions  =====


# --- write your function names in this list ---
for solution in [
    reverse_iterable
]:
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
