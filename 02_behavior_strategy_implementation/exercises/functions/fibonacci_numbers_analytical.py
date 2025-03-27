#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# source: https://github.com/nocotan/algorithm_collection/blob/main/algorithm_collection/mathematics/fibonacci_numbers_analytical.py

# --- import things ---

import math

# --- declare function ---


def fibonacci_numbers_analytical(n):
    return round(pow((1 + math.sqrt(5)) / 2, n) / math.sqrt(5))


# --- test function ---
