""" Initial Value

  write the initial value for sum to pass the assertion

  sum is used as an accumulating variable
    with each iteration it grows
    accumulating the data until it reaches a correct value
"""


print('-- begin --')

# fill in the initial value to pass the assertion
# there are more than 1 correct answer!
# how many can you find?
# what do all the correct answers have in common?
sum = _

while sum < 100:
    if sum % 2 == 0:
        sum += sum
        print('if path:', sum)
    else:
        sum += 1
        print('else path:', sum)

assert sum == 128, 'the sum should be 128'

print('-- end --')
