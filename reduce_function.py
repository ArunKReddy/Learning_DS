import functools

import operator

lst = [1, 3, 5, 7, 8]

# To find the sum of all the numbers of the list.
print("Using lambda Expression, add two numbers : ", functools.reduce(lambda a, b: a+b, lst))

print("Using Operator, add two numbers : ", functools.reduce(operator.add, lst))

# To find the greatest number in the list
print("Using lambda Expression, Finding the greatest number in the list : ", functools.reduce(lambda a, b : a if a > b else b, lst))

# To multiply the list.
print("Using Operator, multiply the list : ", functools.reduce(operator.mul, lst))