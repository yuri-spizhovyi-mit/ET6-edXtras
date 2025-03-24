#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# DEFINING a function creates it in memory
#  without executing the code inside the function body
def i_exist():
    print('I exist!')

# CALLING a function will run the code in its body
# you can do this as many times as you like
i_exist()
i_exist()
i_exist()

# there are 3 prints, and one print statement in the source code
#  print is not run when the function is DEFINED
#  but it is run each time the function is CALLED
