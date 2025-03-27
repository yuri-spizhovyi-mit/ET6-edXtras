#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def a(b):
    assert isinstance(b, str), "argument is not a string"

    c = ""

    for d in b:
        c = d + c

    return c


# --- assertion tests ---
