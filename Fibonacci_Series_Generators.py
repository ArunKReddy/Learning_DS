# Fibonacci without Generators

print("*************Fibonacci without Using Generators********************")


def fibonacci(n):

    if n < 0:
        print("Incorrect Input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print("The fibonacci series is : ", fibonacci(10))

print("******************************************************************************")

print("*************Fibonacci Using Generators********************")


def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a+b


import types

if type(fib()) == types.GeneratorType:
    print("Good, the fib function is a generator..")

    counter = 0
    for n in fib():
        print(n)
        counter +=1
        if counter == 10:
            break

# ******************************************************************************************

# Method 3:
def fibonacci1(n):
    a=0
    b=1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b


print("Third Method : The fibonacci series is : ", fibonacci1(10))