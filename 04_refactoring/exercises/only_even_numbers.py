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
def only_even_numbers(array_of_numbers: list[int | float]) -> list[int | float]:
    assert isinstance(array_of_numbers, list), "argument is not a list"
    assert all(isinstance(item, (int, float)) for item in array_of_numbers), (
        "argument does not contain only numbers"
    )

    return [num for num in array_of_numbers if num % 2 == 0]


#  =====  test your solutions  =====


# --- write your function names in this list ---
for solution in [only_even_numbers]:
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
