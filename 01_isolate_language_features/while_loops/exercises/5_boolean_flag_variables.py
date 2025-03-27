"""Boolean Flag Variable

this exercise contains a variable used as a Boolean Flag

a Boolean Flag is a variable used to keep track of some important condition
it will written in one place to signal something about the program
  the if condition updates it's value if the padded_string is long enough
it will be read in another place to make a decision
  the while loop condition uses it to check if the looping is finished

complete the loop condition and the loop body to pass the assertion
"""

print("-- begin --")

# Constants
long_enough = 14
padding = ".:."

# Accumulator variable
padded_string = "hi"

# Boolean flag variable
islong_enough = False
while __:  # use the flag variable to exit the loop
    padded_string = __
    print(padded_string)

    if __:
        __

assert padded_string == "hi.:..:..:..:.", '"hi" should have 12 padding characters'

print("-- end --")
