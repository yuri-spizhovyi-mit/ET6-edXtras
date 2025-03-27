#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# RETURN VALUES allow you to send values from functions to parent scope
def find_the_type(param):
    return type(param).__name__
    print("nothing after a return statement is executed!")


# to save return values for later, assign them to a variable
returned1 = find_the_type(4.0)
print("returned1:", returned1)

returned2 = find_the_type("4.0")
print("returned2:", returned2)

arg3 = None
returned3 = find_the_type(arg3)
print("returned3:", returned3)

arg4 = False
returned4 = find_the_type(arg4)
print("returned4:", returned4)
