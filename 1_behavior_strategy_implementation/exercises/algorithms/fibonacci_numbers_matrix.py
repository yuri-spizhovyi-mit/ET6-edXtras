#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# source: https://github.com/nocotan/algorithm_collection/blob/main/algorithm_collection/mathematics/fibonacci_numbers_matrix.py

# --- declare helper functions ---


def multiply(F, M):
    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


def power(F, n):
    M = [[1, 1], [1, 0]]

    for i in range(2, n + 1):
        multiply(F, M)

# --- declare primary function ---

def fib(n):
    F = [[1, 1], [1, 0]]
    if (n == 0):
        return 0
    power(F, n - 1)

    return F[0][0]

# --- test function ---
