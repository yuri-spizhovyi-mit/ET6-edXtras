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
import math


#  =====  write and refactor your solutions  =====


# --- initial solution to refactor ---
def sum_numbery(list_of_number_strings: list[str]) -> float:
    assert isinstance(list_of_number_strings, list), "argument is not a list"
    assert all(isinstance(item, str) for item in list_of_number_strings), (
        "argument contains non-strings"
    )

    numbers = []
    for s in list_of_number_strings:
        try:
            num = float(s)
            if not math.isnan(num):
                numbers.append(num)
        except ValueError:
            pass

    return sum(numbers)


#  =====  test your solutions  =====


# --- write your function names in this list ---
for solution in [sum_numbery]:
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
