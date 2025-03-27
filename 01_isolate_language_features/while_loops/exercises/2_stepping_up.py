"""Stepping Up

Stepper Variables change systematically,
  going through a series of values for control flow

"Stepper" describes how you are using a variable
  this term is not a JavaScript thing
  it's a general programming concept


fill in the loop condition and update the stepper variable
"""

print("-- begin --")

to_repeat = "howdy"
total_repetitions = 4

repeated_string = ""

# Stepper variable for counting repetitions
i = 0
while __:
    repeated_string = __
    print(repeated_string)

    __  # Increment the stepper variable

assert repeated_string == "howdyhowdyhowdyhowdy", '"howdy" should be repeated 4 times'

print("-- end --")
