#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The call stack happens when you call a function from inside a function call
# This is much easier to visualize than to describe, so try using ...
#   the debugger, trace & Python Tutor!

call_stack_root = 0


def func1(depth):
    print("entering func1")
    print("depth:", depth)
    print("leaving func1")


print("this call stack will be 1 call deep")
func1(call_stack_root + 1)


def func2(depth):
    print("entering func2")
    func1(depth + 1)
    print("leaving func2")


# it's backwards from what you might expect
#  func2 will open first, but func1 will close first
print("this call stack will be 2 calls deep")
func2(call_stack_root + 1)


def func3(depth):
    print("entering func3")
    func2(depth + 1)
    print("leaving func3")


print("this call stack will be 3 calls deep")
func3(call_stack_root + 1)
