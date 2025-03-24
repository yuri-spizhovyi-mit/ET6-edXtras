#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Error messages printed to the console log the call stack
# Study this example in the debugger
# Compare what you see in the "call stack" debugger tab to what's logged

call_stack_root = 0

def func1(depth):
    print('entering func1')
    if depth == 3:
        raise Exception('read the call stack!')
    print('leaving func1')

print('this call stack will be 1 call deep')
func1(call_stack_root + 1)


def func2(depth):
    print('entering func2')
    func1(depth + 1)
    print('leaving func2')

print('this call stack will be 2 calls deep')
func2(call_stack_root + 1)


def func3(depth):
    print('entering func3')
    func2(depth + 1)
    print('leaving func3')

print('this call stack will be 3 calls deep')
func3(call_stack_root + 1)
