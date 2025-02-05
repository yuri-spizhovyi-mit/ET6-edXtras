""" anatomy of a while loop: https://www.programiz.com/python-programming/while-loop#flowchart
  while _condition_:
    _loop_body_

"""

# step 1
print('-- begin --')

# 2: Declare and assign a
a = 0

# 3, 5, 7, 9, 11: Evaluate the condition
while a < 4:
    # 4, 6, 8, 10: Increment a
    a = a + 1

# 12: Assert a (Python uses 'assert' slightly differently)
assert a == 4, 'a should be 4'

# 13
print('-- end --')
