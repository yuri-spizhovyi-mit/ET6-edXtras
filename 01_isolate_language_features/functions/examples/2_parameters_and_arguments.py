#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Functions allow you to reuse the same code with different values
# PARAMETERS declare variables available inside your function
# They are assigned a value when you CALL the function
def log_the_parameter(parameter):
    print(type(parameter).__name__, parameter)


# ARGUMENTS assign values to parameters when functions are CALLED
# you can pass arguments directly as values
log_the_parameter("4")
log_the_parameter(4.0)
log_the_parameter("4.0")

# or indirectly using variables
arg1 = True
log_the_parameter(arg1)

arg2 = False
log_the_parameter(arg2)

arg3 = None
log_the_parameter(arg3)

# if no argument is passed, an exception is raised
log_the_parameter()
