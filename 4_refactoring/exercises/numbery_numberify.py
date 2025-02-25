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
def numbery_numberify(array_of_strings: list[str]) -> list[float]:
    assert isinstance(array_of_strings, list), "argument is not a list"
    assert all(
        isinstance(item, str) for item in array_of_strings
    ), "argument contains non-strings"

    numbers = [
        float(s)
        for s in array_of_strings
        if s.strip()
        and not (s.strip().startswith("nan") or s.strip().lower() == "infinity")
    ]
    return [n for n in numbers if not math.isnan(n)]


#  =====  test your solutions  =====


# --- write your function names in this list ---
for solution in [numbery_numberify]:
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
