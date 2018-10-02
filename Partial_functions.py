from functools import partial


def multiply(x, y):
    return x * y

# default values will start replacing variables from the left. The 2 will be replace x, y will
# equal 4 when dbl(4) is called. Its doesn't make any difference.


dbl = partial(multiply, 2)
print(dbl(4))


# One more example.

def func(u, v, w, x):
    return u*2 + v*3 + w*4 + x*5


f = partial(func, 1, 2)
print("Partial functions : ", f(3, 4))