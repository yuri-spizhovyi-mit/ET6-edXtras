#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# source: https://github.com/nocotan/algorithm_collection/blob/main/algorithm_collection/mathematics/fibonacci_numbers_optimized.py


# --- declare globals ---

MAX = 1000
f = [0] * MAX

# --- declare function ---


def fibonacci_numbers_optimized(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        f[n] = 1
        return f[n]

    if f[n]:
        return f[n]

    if n & 1:
        k = (n + 1) // 2
    else:
        k = n // 2

    if n & 1:
        f[n] = fib(k) * fib(k) + fib(k - 1) * fib(k - 1)
    else:
        f[n] = (2 * fib(k - 1) + fib(k)) * fib(k)

    return f[n]


# --- test function ---
