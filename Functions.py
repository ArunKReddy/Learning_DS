
#################################################################
# Multiplication table.
def multiply(number):
    n = 1
    while n <= 10.0:
        print('Multiply by', number, n, '\t', n * number)
        n = n + 1


def multiplication():
    number = 1
    while number <= 6:  
        multiply(number)
        number = number + 1


multiplication()

###################################################################
import math
x = 1.0
while x < 10.0:
    print(x, '\t', math.log(x))
    x = x + 1.0


################################################################
# Recursion of a number
def recursion(n):
    if n == 0:
        print('Blast Off!!!')
    else:
        print(n)
        recursion(n-1)


recursion(5)
#################################################################

##################################################################
# Factorial of a Number

def fact(n):
    if n == 0:
        return 1
    else:
        recurse = fact(n-1)
        result = recurse * n
        return result

Factorial = fact(5)
print("Factorial of a number : ", Factorial)
####################################################################










#####################################################################
#####checking whether the number is divisable or not#################

def IsDivisable(x, y):
    if x % y == 0:
        return True
    else:
        return False


IsD = IsDivisable(6, 2)
print(IsD)
#####################################################################

###########################################################
#To find the distance
import math

def distance(x1, y1, x2, y2):
    dx = x2-x1
    dy = y2-y1
    print("Dx : ", dx)
    print("Dy : ", dy)
    squarednumber = dx ** 2 + dy ** 2
    dist = math.sqrt(squarednumber)
    return dist


d = distance(1, 2, 4, 6)
print("Squared value : ", d)
#############################################################






# a = type("32")
# print(a)
#
# print(float(3))
#
# minute = 59
# print(minute/60)


#Math Functions
# import math
#
# print(math.sqrt(2)/2.0)
#
#
# def threenewLines():
#     newLine()
#     newLine()
#     newLine()
#
# def newLine():
#     print(" ")
#
# print('First Line')
# threenewLines()
# print('Second Line')
#
# def printTwice(bruce):
#     print(bruce, bruce)
#
# printTwice('Spam')
#
# print('spam'*4)
#
#
# michael = 'Eric, the half of bee. '
# printTwice(michael)
#
# def catTwice(part1,part2):
#     cat = part1 + part2
#     printTwice(cat)
#
# catTwice('Akruthi','Aishu')
