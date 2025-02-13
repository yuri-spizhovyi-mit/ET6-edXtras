#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" """

# --- declare function ---


def a(b: list) -> list:
    """Creates a reversed copy of a list"""
    c = []
    for item in b:
        c.insert(0, item)
    return c


# --- test function ---
