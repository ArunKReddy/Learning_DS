import itertools

lis = [1, 4, 7, 3]

print("The summation of the list using accumulate : ", list(itertools.accumulate(lis, lambda x, y: x+y)))